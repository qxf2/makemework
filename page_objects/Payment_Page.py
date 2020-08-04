from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Payment_Page(Base_Page):
    FORM_EMAIL_ID = locators.FORM_EMAIL_ID
    FORM_ACCOUNT_NUMBER = locators.FORM_ACCOUNT_NUMBER
    FORM_EXPIRY_DATE =  locators.FORM_EXPIRY_DATE
    FORM_CVV = locators.FORM_CVV
    FORM_ZIP_CODE = locators.FORM_ZIP_CODE
    FORM_REMEMBER_ME = locators.FORM_REMEMBER_ME
    FORM_MOBILE = locators.FORM_MOBILE
    FORM_SUBMIT = locators.FORM_SUBMIT

    def start(self):
        "Switching to payment iframe"
        self.switch_frame("iframe")

    def click_pay_button(self):
        "Click to the pay button"
        result_flag = self.click_element(self.CART_PAY_BUTTON)
        if result_flag:
            self.switch_page("checkout")
        self.conditional_write(result_flag,
        positive="Clicked on the Pay with card button",
        negative="Could not click on the Pay with card button")

        return result_flag

    @Wrapit._exceptionHandler
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.FORM_EMAIL_ID,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_account_number(self,account_number):
        "Set the account number on the form"
        result_flag = self.set_text(self.FORM_ACCOUNT_NUMBER,account_number)
        self.conditional_write(result_flag,
            positive='Set the account number to: %s'%account_number,
            negative='Failed to set the account number in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_expiry_date(self,expiry_date):
        "Set the expiry date on the form"
        result_flag = self.set_text(self.FORM_EXPIRY_DATE,expiry_date)
        self.conditional_write(result_flag,
            positive='Set the expiry date to: %s'%expiry_date,
            negative='Failed to set the expiry date in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_cvv(self,cvv):
        "Set the cvv on the form"
        result_flag = self.set_text(self.FORM_CVV,cvv)
        self.conditional_write(result_flag,
            positive='Set the cvv to: %s'%cvv,
            negative='Failed to set the cvv in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_zip_code(self,zip_code):
        "Set the zip code on the form"
        result_flag = self.set_text(self.FORM_ZIP_CODE,zip_code)
        self.conditional_write(result_flag,
            positive='Set the zip code to: %s'%zip_code,
            negative='Failed to set the zip code in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_mobile(self,mobile):
        "Set the mobile number on the form"
        result_flag = self.set_text(self.FORM_MOBILE,mobile)
        self.conditional_write(result_flag,
            positive='Set the mobile number to: %s'%mobile,
            negative='Failed to set the mobile number in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def click_submit_button(self):
        "Click the pay button"
        result_flag = self.click_element(self.FORM_SUBMIT)
        self.conditional_write(result_flag,
        positive="Clicked on the submit button",
        negative="Could not click on the submit button")

        return result_flag
