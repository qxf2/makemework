#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the Main page
TEMPERATURE_FIELD = "id,temperature"
BUY_BUTTON = "xpath,//button[contains(text(),'Buy %s')]"

#Product page
PAGE_HEADING = "xpath,//h2[text()='%s']"
PRODUCTS_LIST = "xpath,//div[contains(@class,'col-4')]"
ADD_PRODUCT_BUTTON = "xpath,//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"
CART_QUANTITY_TEXT = "id,cart"
CART_BUTTON = "xpath,//button[@onclick='goToCart()']"

#Cart page
CART_TITLE = "xpath,//h2[text()='Checkout']"
CART_ROW = "xpath,//tbody/descendant::tr"
CART_ROW_COLUMN = "xpath,//tbody/descendant::tr[%d]/descendant::td"
CART_TOTAL = "id,total"

#Payment page
CARD_NUMBER = "xpath,//div[@class='Textbox-inputRow']/descendant::input[@placeholder='Card number']"
CARD_EXPIRY = "xpath,//div[@class='Textbox-inputRow']/descendant::input[@placeholder='MM / YY']"
CHECKBOX = "xpath,//a[@class='Checkbox']"
CVC = "xpath,//div[@class='Textbox-inputRow']/descendant::input[@placeholder='CVC']"
EMAIL = "xpath,//input[@type='email']"
MANUAL_ENTRY_BUTTON = "xpath,//div[@class='CodeNotReceived-actionMessage']/descendant::span"
PHONE_NUMBER = "xpath,//div[@class='Textbox-inputRow']/descendant::input[@inputmode='tel']"
PAY_BUTTON = "xpath,//div[@class='Section-button']/button"
PAY_WITH_CARD = "xpath,//button/span[contains(text(),'Pay with Card')]"
PAYMENT_MESSAGE = "xpath,//body/descendant::h2"
REMEMBER_ME = "xpath,//a[@class='Checkbox']"
SWITCH_FRAME = "xpath,//iframe[contains(@name,'stripe_checkout_app')]"
VERIFICATION_MESSAGE ="xpath,//form[@class='Modal-form']/descendant::span[contains(text(),'Enter the verification code')]"
ZIP_CODE = "xpath,//div[@class='Textbox-inputRow']/descendant::input[@placeholder='ZIP Code']"