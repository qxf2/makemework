"""
This module models the Moisturizers page
URL: /moisturizer
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from .Product_Object import Product_Object

class Moisturizers_Page(Base_Page, Product_Object):
    "This class models the moisturizer page"
    def start(self):
        "Go to this URL -- if needed"
        url = 'moisturizer'
        self.open(url)


