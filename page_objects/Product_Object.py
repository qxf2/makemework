"""
This Object models the product page.
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Product():
    "A product class"
    def __init__(self,name,price):
        "Set up the product with name and price"
        self.name = name 
        self.price = price 

class Product_Object():
    "Page Object for the products object"
    PRODUCTS_LIST = locators.PRODUCTS_LIST
    ADD_PRODUCT_BUTTON = locators.ADD_PRODUCT_BUTTON
    CART_QUANTITY_TEXT = locators.CART_QUANTITY_TEXT
    CART_BUTTON = locators.CART_BUTTON
    CART_TITLE = locators.CART_TITLE
    CART_QUANTITY = 0
    PRODUCTS_PER_PAGE = 6

    def convert_str_to_int(self,string, default=100000, expect_fail=False):
        "Convert a given string to integer. Return default if you cannot convert"
        try:
            integer = int(string)
        except Exception as e:
            if not expect_fail:
                self.write("Unable to convert the string %s into a number"%string)
            integer = default

        return integer

    @Wrapit._exceptionHandler
    def get_product_name(self,product_text):
        "Parse the product name from the product text"
        name = product_text.split(b"\n")[0].strip()
        name = name.decode('ascii')

        return name 

    @Wrapit._exceptionHandler
    def get_product_price(self,product_text):
        "Parse the product price from the product text"
        price = product_text.split(b"Price: ")[-1]
        price = price.split(b"Rs.")[-1]
        price = price.split(b"\n")[0]
        price = price.decode('ascii')
        price = self.convert_str_to_int(price,default=100000)

        return price

    @Wrapit._screenshot
    def get_all_products_on_page(self):
        "Get all the products"
        result_flag = False 
        all_products = []
        product_list = self.get_elements(self.PRODUCTS_LIST)
        for i,product in enumerate(product_list):
            product_text = self.get_dom_text(product)
            name = self.get_product_name(product_text)
            price = self.get_product_price(product_text)
            all_products.append(Product(name, price))
        if self.PRODUCTS_PER_PAGE == len(all_products):
            result_flag = True 
        self.conditional_write(result_flag,
        positive="Obtained all %d products from the page"%self.PRODUCTS_PER_PAGE,
        negative="Could not obtain all products. Automation got %d products while we expected %d products"%(len(all_products),self.PRODUCTS_PER_PAGE))

        return all_products
    
    def print_all_products(self):
        "Print out all the products nicely"
        all_products = self.get_all_products_on_page()
        self.write("Product list is: ")
        for product in all_products:
            self.write("%s: %d"%(product.name,product.price))

    def get_minimum_priced_product(self,filter_condition):
        "Return the least expensive item based on a filter condition"
        minimum_priced_product = None 
        min_price = 10000000
        min_name = ''
        all_products = self.get_all_products_on_page()
        for product in all_products:
            if filter_condition.lower() in product.name.lower():
                if product.price <= min_price:
                    minimum_priced_product = product
                    min_price = product.price
                    min_name = product.name 
        result_flag = True if minimum_priced_product is not None else False 
        self.conditional_write(result_flag,
        positive="Min price for product with '%s' is %s with price %d"%(filter_condition,min_name,min_price),
        negative="Could not obtain the cheapest product with the filter condition '%s'\nCheck the screenshots to see if there was at least one item that satisfied the filter condition."%filter_condition)

        return minimum_priced_product
            
    def click_add_product_button(self,product_name):
        "Click on the add button corresponding to the name"
        result_flag = self.click_element(self.ADD_PRODUCT_BUTTON%product_name)
        self.conditional_write(result_flag,
        positive="Clicked on the add button to buy: %s"%product_name,
        negative="Could not click on the add button to buy: %s"%product_name)

        return result_flag

    @Wrapit._screenshot
    def get_current_cart_quantity(self):
        "Return the number of items in the cart"
        cart_text = self.get_text(self.CART_QUANTITY_TEXT)
        cart_quantity = cart_text.split()[0]
        cart_quantity = cart_quantity.decode('ascii')
        empty_cart_flag = True if self.CART_QUANTITY == 0 else False
        cart_quantity = self.convert_str_to_int(cart_quantity, default=0, expect_fail = empty_cart_flag)
        self.CART_QUANTITY = cart_quantity
        self.conditional_write(True,
        positive="The cart currently has %d items"%self.CART_QUANTITY,
        negative="")
        return cart_quantity

    def add_product(self,product_name):
        "Add the lowest priced product with the filter condition in name"
        before_cart_quantity = self.get_current_cart_quantity() 
        result_flag = self.click_add_product_button(product_name)
        after_cart_quantity = self.get_current_cart_quantity()
        result_flag &= True if after_cart_quantity - before_cart_quantity == 1 else False 

        return result_flag

    @Wrapit._screenshot
    def click_cart_button(self):
        "Click the cart button"
        result_flag = self.click_element(self.CART_BUTTON)
        self.conditional_write(result_flag,
        positive="Clicked on the cart button",
        negative="Could not click on the cart button")

        return result_flag

    @Wrapit._screenshot
    def verify_cart_page(self):
        "Verify automation is on the cart page"
        result_flag = self.smart_wait(5,self.CART_TITLE)
        self.conditional_write(result_flag,
        positive="Automation is on the Cart page",
        negative="Automation is not able to locate the Cart Title. Maybe it is not even on the cart page?")
        if result_flag:
            self.switch_page("main")

        return result_flag

    def go_to_cart(self):
        "Go to the cart page"
        result_flag = self.click_cart_button()
        result_flag &= self.verify_cart_page()

        return result_flag