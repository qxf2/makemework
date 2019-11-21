"""
This class models the landing page.
URL: /
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit

class Landing_Page(Base_Page):
    "Page Object for the landing page"
    
    def start(self):
        "Go to the landing page"
        url = ''
        self.open(url)