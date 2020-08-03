"""
This class models the Contact page.
URL: contact
The page consists of a header, footer and form object.
"""
from .Base_Page import Base_Page
from .contact_form_object import Contact_Form_Object
#from .header_object import Header_Object
#from .footer_object import Footer_Object
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Contact_Page(Base_Page,Contact_Form_Object):#,Header_Object,Footer_Object):
    "Page Object for the contact page"
    FORM_EMAIL_ID = locators.FORM_EMAIL_ID

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'contact'
        self.open(url)

    @Wrapit._exceptionHandler
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.FORM_EMAIL_ID,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag
