from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import config.config_path as locators
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://weathershopper.pythonanywhere.com/")

# getting the value for temperature
temperature=locators.temperature
# getting the xpath for moisturizer button
moisturizer=locators.moisturizer_button
#getting the xpath for sunscreen button
sunscreen=locators.sunscreen_button
 # getting the xpath for cart button
cart=locators.cart_button
# getting the xpath for pay button
pay=locators.pay_button
# getting the xpath for price
price=locators.price_list

temp = driver.find_element(By.XPATH,temperature)
temp_txt = int((temp.text)[0:2])
print (temp_txt)
price_list=[]
least_price_item = 1000

# get the least price value
def get_minimum_value():
    for item in items:
        print(item)
        item_price=int((item.text)[-3::])
        price_list.append(item_price)
    print(price_list)
    value = str(min(price_list))
    print(value)
    product_text = item.find_element(By.XPATH,"//p[contains(text(),'"+value+"')]/following-sibling::button[@class='btn btn-primary']").click()


if (temp_txt) < (20) :
    print("Moisturizer products")
    driver.find_element(By.XPATH,moisturizer).click()
    items= driver.find_elements(By.XPATH,price)
    get_minimum_value()

elif (temp_txt)> (20): 
    print("Sunscreen products")
    driver.find_element(By.XPATH,sunscreen).click()   
    items= driver.find_elements(By.XPATH,price)
    get_minimum_value()


    
driver.find_element(By.XPATH,value=cart).click()
time.sleep(2)
# Click pay with card button
print(pay)
driver.find_element(By.XPATH,value=pay).click()

