from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.get('https://www.yhd.com')
a=driver.find_elements(By.CLASS_NAME,'bursting')
js='window.scrollTo(0,1300)'
driver.execute_script(js)
for i in a :
    if i.get_attribute('clstag')=='pageclick|keycount|shouye_20181018|scenario3_sku4':
        i.click()

