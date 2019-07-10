"""
This module models the Sunscreens page
URL: /sunscreen
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from .Product_Object import Product_Object

class Sunscreens_Page(Base_Page, Product_Object):
    "This class models the sunscreen page"
    def start(self):
        "Go to this URL -- if needed"
        url = 'sunscreen'
        self.open(url)
