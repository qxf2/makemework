"""
This class models the landing page of Weather Shopper.
URL: /
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators 

class Main_Page(Base_Page):
    "Page Object for the main page"
    #locators
    TEMPERATURE_FIELD = locators.TEMPERATURE_FIELD
    BUY_BUTTON = locators.BUY_BUTTON
    PAGE_HEADING = locators.PAGE_HEADING

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)

    @Wrapit._screenshot
    def get_temperature(self):
        "Return the temperature listed on the landing page"
        result_flag = False 
        temperature = self.get_text(self.TEMPERATURE_FIELD)
        if temperature is not None:
            self.write("The temperature parsed is: %s"%temperature,level="debug")
            #Strip away the degree centigrade
            temperature = temperature.split()[0] 
            
            try:
                temperature = int(temperature)
            except Exception as e:
                self.write("Error type casting temperature to int",level="error")
                self.write("Obtained the temperature %s"%temperature)
                self.write("Python says: " + str(e))
            else:
                result_flag = True
        else:
            self.write("Unable to read the temperture.",level="")
        self.conditional_write(result_flag,
        positive="Obtained the temperature: %d"%temperature,
        negative="Could not obtain the temperature on the landing page.")
        
        return temperature

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_buy_button(self,product_type):
        "Choose to buy moisturizer or sunscreen"
        result_flag = False 
        product_type = product_type.lower()
        if product_type in ['sunscreens','moisturizers']:
            result_flag = self.click_element(self.BUY_BUTTON%product_type)
            self.conditional_write(result_flag,
            positive="Clicked the buy button for %s"%product_type,
            negative="Could not click the buy button for %s"%product_type)
            result_flag &= self.smart_wait(5,self.PAGE_HEADING%product_type.title())
            if result_flag:
                self.switch_page(product_type)

        self.conditional_write(result_flag,
        positive="Automation is on the %s page"%product_type.title(),
        negative="Automation could not navigate to the %s page"%product_type.title())

        return result_flag