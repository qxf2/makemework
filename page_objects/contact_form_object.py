"""
This class models the form on contact page
The form consists of some input fields.
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Contact_Form_Object:
    "Page object for the contact Form"

    #locators
    #contact_name_field = locators.contact_name_field
    FORM_EMAIL_ID = locators.FORM_EMAIL_ID
    FORM_ACCOUNT_NUMBER = locators.FORM_ACCOUNT_NUMBER
    FORM_EXPIRY_DATE =  locators.FORM_EXPIRY_DATE
    FORM_CVV = locators.FORM_CVV
    FORM_ZIP_CODE = locators.FORM_ZIP_CODE
    FORM_REMEMBER_ME = locators.FORM_REMEMBER_ME
    FORM_MOBILE = locators.FORM_MOBILE
    FORM_SUBMIT = locators.FORM_SUBMIT

    @Wrapit._exceptionHandler
    def set_name(self,name):
        "Set the name on the Kick start form"
        result_flag = self.set_text(self.contact_name_field,name)
        self.conditional_write(result_flag,
            positive='Set the name to: %s'%name,
            negative='Failed to set the name in the form',
            level='debug')

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

    @Wrapit._screenshot
    def click_pay_button(self):
        "Click the pay button"
        result_flag = self.click_element(self.FORM_SUBMIT)
        self.conditional_write(result_flag,
        positive="Clicked on the pay button",
        negative="Could not click on the pay button")

        return result_flag