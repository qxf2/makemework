"""
This module models the cart page on weather shopper
URL: /cart
"""

from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators
import conf.payment_details_conf as paymentdetails

class Cart_Page(Base_Page):
    "This class models the cart page"

    CART_ROW = locators.CART_ROW
    CART_ROW_COLUMN = locators.CART_ROW_COLUMN
    CART_TOTAL = locators.CART_TOTAL
    COL_NAME = 0
    COL_PRICE = 1
    PAY_WITH_CARD = locators.PAY_WITH_CARD
    EMAIL = locators.EMAIL
    CARD_NUMBER = locators.CARD_NUMBER
    CARD_EXPIRY = locators.CARD_EXPIRY
    CVC = locators.CVC
    ZIP_CODE = locators.ZIP_CODE
    PHONE_NUMBER = locators.PHONE_NUMBER
    REMEMBER_ME = locators.REMEMBER_ME
    PAY_BUTTON = locators.PAY_BUTTON
    PAYMENT_MESSAGE = locators.PAYMENT_MESSAGE
    MANUAL_ENTRY_BUTTON = locators.MANUAL_ENTRY_BUTTON
    VERIFICATION_MESSAGE = locators.VERIFICATION_MESSAGE



    def start(self):
        "Override the start method of base"
        url = "cart"
        self.open(url)

    def process_item(self,item):
        "Process the given item"
        #Convert the price to an int
        try:
            item[self.COL_PRICE] = int(item[self.COL_PRICE])
        except Exception as e:
            self.write("Unable to convert the string %s into a number"%item[self.COL_PRICE])

        return item 

    def get_cart_items(self):
        "Get all the cart items as a list of [name,price] lists"
        cart_items = []
        row_elements = self.get_elements(self.CART_ROW)
        for index,row in enumerate(row_elements):
            column_elements = self.get_elements(self.CART_ROW_COLUMN%(index+1))
            item = []
            for col in column_elements:
                text = self.get_dom_text(col)
                item.append(text.decode('ascii'))
            item = self.process_item(item)
            cart_items.append(item)

        return cart_items

    def verify_cart_size(self,expected_cart,actual_cart):
        "Make sure expected and actual carts have the same number of items"
        result_flag = False 
        if len(expected_cart) == len(actual_cart):
            result_flag = True
        self.conditional_write(result_flag,
        positive="The expected cart and actual cart have the same number of items: %d"%len(expected_cart),negative="The expected cart has %d items while the actual cart has %d items"%(len(expected_cart),len(actual_cart)))

        return result_flag
    
    def verify_extra_items(self,expected_cart,actual_cart):
        "Items which exist in actual but not in expected"
        item_match_flag = True 
        for item in actual_cart:
            #Does the item exist in the product list
            found_flag = False 
            price_match_flag = False 
            expected_price = 0
            for product in expected_cart:
                if product.name == item[self.COL_NAME]:
                    found_flag = True
                    if product.price == item[self.COL_PRICE]:
                        price_match_flag = True 
                    else:
                        expected_price = product.price
                    break
            self.conditional_write(found_flag,
            positive="Found the expected item '%s' in the cart"%item[self.COL_NAME],
            negative="Found an unexpected item '%s' in the cart"%item[self.COL_NAME])

            self.conditional_write(price_match_flag,
            positive="... the expected price matched to %d"%item[self.COL_PRICE],
            negative="... the expected price did not match. Expected: %d but Obtained: %d"%(expected_price,item[self.COL_PRICE]))

            item_match_flag &= found_flag and price_match_flag
        
        return item_match_flag

    def verify_missing_item(self,expected_cart,actual_cart):
        "Verify if expected items are missing from the cart"
        item_match_flag = True
        for product in expected_cart:
            price_match_flag = False
            found_flag = False
            actual_price = 0 
            for item in actual_cart:
                if product.name == item[self.COL_NAME]:
                    found_flag = True
                    if product.price == item[self.COL_PRICE]:
                        price_match_flag = True 
                    else:
                        actual_price = item[self.COL_PRICE]
                    break    
            item_match_flag &= found_flag and price_match_flag
            self.conditional_write(found_flag,
            positive="Found the expected item '%s' in the cart"%product.name,
            negative="Did not find the expected item '%s' in the cart"%product.name)
            self.conditional_write(price_match_flag,
            positive="... the expected price matched to %d"%product.price,
            negative="... the expected price did not match. Expected: %d but Obtained: %d"%(product.price,actual_price)) 

        return item_match_flag

    def get_total_price(self):
        "Return the cart total"
        actual_price = self.get_text(self.CART_TOTAL)
        actual_price = actual_price.decode('ascii')
        actual_price = actual_price.split('Rupees')[-1]
        try:
            actual_price = int(actual_price)
        except Exception as e:
            self.write("Could not convert '%s' (cart total price) into an integer"%actual_price)

        return actual_price

    def verify_cart_total(self,expected_cart):
        "Verify the total in the cart"
        expected_total = 0
        for product in expected_cart:
            expected_total = product.price 
        actual_total = self.get_total_price()
        result_flag = actual_total == expected_total
        self.conditional_write(result_flag,
        positive="The cart total displayed is correct",
        negative="The expected and actual cart totals do not match. Expected: %d, actual: %d"%(expected_total, actual_total))

        return result_flag

    def verify_cart(self,expected_cart):
        "Verify the (name,price) of items in cart and the total"
        actual_cart = self.get_cart_items()
        result_flag = self.verify_cart_size(expected_cart,actual_cart)
        result_flag &= self.verify_extra_items(expected_cart,actual_cart)
        if result_flag is False:
            result_flag &= self.verify_missing_item(expected_cart,actual_cart)
        result_flag &= self.verify_cart_total(expected_cart)

        return result_flag 
    
    def click_pay_button(self):
        "Click the 'Pay with Card' button"
        self.click_element(self.PAY_WITH_CARD)

        
    
    


    def make_payment(self,email,card_number,card_expiry,card_cvc,zip_code,phone_number):
        "Fill the payment details"
        self.switch_frame(name='stripe_checkout_app')
    
        self.wait(2)
        self.set_text(self.EMAIL,email)
        self.wait(4)
    
        try:
            message = self.get_text(self.VERIFICATION_MESSAGE)
            self.wait(3)
            if 'Enter the verification code' in message.decode('utf-8'):
                self.click_element(self.MANUAL_ENTRY_BUTTON)
                self.wait(3)
        except:
            print("Enter details manually")
        
        finally:
            self.set_text(self.CARD_NUMBER,card_number)
            self.set_text(self.CARD_EXPIRY,card_expiry)
            self.set_text(self.CVC,card_cvc)
            self.set_text(self.ZIP_CODE,zip_code)
            self.select_checkbox(self.REMEMBER_ME)
            self.set_text(self.PHONE_NUMBER,phone_number)
            self.click_element(self.PAY_BUTTON)


        self.switch_frame_to_window()
        self.wait(4)
       
    def check_payment_status(self):
        "Check the payment status"      
        message = self.get_text(self.PAYMENT_MESSAGE)
        
        if(message.decode('utf-8') == 'PAYMENT SUCCESS'):
            return True
        elif(message.decode('utf-8') == 'PAYMENT FAILED'):
            return False
        


        

