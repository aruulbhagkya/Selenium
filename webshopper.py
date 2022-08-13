from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\Users\\Ram\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://weathershopper.pythonanywhere.com/")
test = driver.find_element(By.XPATH,"//span[@id='temperature']")
print (test.text)

if (test.text)<=('20°C'):
 print("temperature is very cool")
 driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
 driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/button").click()
   
elif (test.text)>=('20°C') :
 print("temperature is very hot")
driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/a/button").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/button").click()
