import chromedriver_binary #For RHEL

from selenium import webdriver
from bs4 import BeautifulSoup
from csv import writer
s_string = input("Search String:: ")
options = webdriver.ChromeOptions().add_argument("--headless")
driver =  webdriver.Chrome(options=options)
driver.get('https://www.amazon.in/')
driver.implicitly_wait(10.00)
driver.find_element_by_id('twotabsearchtextbox').send_keys(s_string)
driver.find_element_by_id('nav-search-submit-button').click()
driver.implicitly_wait(10.00)
cards = driver.find_elements(by=webdriver.common.by.By.XPATH , value='//div[starts-with(@data-component-type,"s-search-result")]')
products = []
for i in cards:
    product = BeautifulSoup(str(i.get_attribute('innerHTML')) , "html.parser")
    info = {'Name': product.h2.a.span.text , 'Price':product.select_one('.a-price-whole')}
    if(type(info['Price']) != type(None) ):
        products.append([info['Name'],info['Price'].text])
print('Product Info Spawned')
with open('links.csv' , 'w' ,newline='\n') as f:
    row_write = writer(f)
    row_write.writerows(products)
driver.quit()
