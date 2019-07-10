"""
This is a broadstack test for Weather Shopper.

This test will:
a) visit the main page
b) get the temperature
c) based on temperature choose to buy sunscreen or moisturizer
d) add products based on some specified logic
e) verify the cart
f) make a payment
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.e2e_weather_shopper_conf as conf

def test_e2e_weather_shopper(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #Create a test object and fill the example form.
        test_obj = PageFactory.get_page_object("Main Page",base_url=base_url)

        #Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)  

        #Read the temperature
        temperature = test_obj.get_temperature()
        result_flag = False
        if type(temperature) == int:
            result_flag = True 
        test_obj.log_result(result_flag,
        positive="Obtained the temperature from the landing page",
        negative="Could not to parse the temperature on the landing page.",
        level="critical")
        
        #Choose the right product type
        product_type = ""
        if temperature <= 18:
            product_type = "moisturizers"
        if temperature >= 34:
            product_type = "sunscreens"
        result_flag = test_obj.click_buy_button(product_type)
        test_obj.log_result(result_flag,
        positive="Landed on the %s page after clicking the buy button"%product_type,
        negative="Could not land on the %s page after clicking the buy button"%product_type,
        level="critical")

        #Add products
        product_filter_list = conf.PURCHASE_LOGIC[product_type]
        product_list = []
        for filter_condition in product_filter_list:
            cheapest_product = test_obj.get_minimum_priced_product(filter_condition)
            product_list.append(cheapest_product)
            result_flag = test_obj.add_product(cheapest_product.name)
            test_obj.log_result(result_flag,
            positive="Added the cheapest product '%s' with '%s'"%(cheapest_product.name,filter_condition),
            negative="Could not add the cheapest product '%s' with '%s'"%(cheapest_product.name,filter_condition))

        #Go to the cart
        result_flag = test_obj.go_to_cart()
        test_obj.log_result(result_flag,
        positive="Automation is now on the cart page",
        negative="Automation is not on the cart page",
        level="critical")

        #Verify the products displayed on the cart page
        result_flag = test_obj.verify_cart(product_list)
        test_obj.log_result(result_flag,
        positive="Something wrong with the cart. The log messages above will have the details",
        negative="Something wrong with the cart. The log messages above will have the details",
        level="critical")

        #Print out the results
        test_obj.write_test_summary()

        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.past_counter
        test_obj.teardown()
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%repr(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_e2e_weather_shopper(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        testrail_flag=options.testrail_flag,
                        tesults_flag=options.tesults_flag,
                        test_run_id=options.test_run_id,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name) 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())