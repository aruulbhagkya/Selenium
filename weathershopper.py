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
moisturizer_button=locators.moisturizer_button
#getting the xpath for sunscreen button
sunscreen_button=locators.sunscreen_button
 # getting the xpath for cart button
cart_button=locators.cart_button
# getting the xpath for pay button
pay_button=locators.pay_button
# getting the xpath for price
price_text=locators.price_list

temp = driver.find_element(By.XPATH,temperature)
temp_txt = int((temp.text)[0:2])
print (temp_txt)
price_list=[]
least_price_item = 1000

# get the least price value
   def click_add_button():
    for item in items:
        print(item)
        item_price=int((item.text)[-3::])
        price_list.append(item_price)
    print(price_list)
    value = str(min(price_list))
    print(value)
    item.find_element(By.XPATH,"//p[contains(text(),'"+value+"')]/following-sibling::button[@class='btn btn-primary']").click()


if (temp_txt) < (20) :
    print("Moisturizer products")
    driver.find_element(By.XPATH,moisturizer_button).click()
    items= driver.find_elements(By.XPATH,price_text)
    click_add_button()

elif (temp_txt)> (20): 
    print("Sunscreen products")
    driver.find_element(By.XPATH,sunscreen_button).click()   
    items= driver.find_elements(By.XPATH,price_text)
    click_add_button()


    
driver.find_element(By.XPATH,value=cart_button).click()
time.sleep(2)
# Click pay with card button
driver.find_element(By.XPATH,value = pay_button).click()
time.sleep(2)
driver.close()
