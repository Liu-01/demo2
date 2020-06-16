from selenium.webdriver.common.by import By

from base.base_action import Base_action
from base.base_driver import Init_driver

class Api_page(Base_action):
    def __init__(self,driver):
        Base_action.__init__(self,driver)

    def open1(self):
        self.open_url('https://www.jisuapi.com/my/login')
    def click2(self):
        self.click(By.LINK_TEXT,'登录')
    def send_keys3(self,keysToSend):
        self.send_keys(By.NAME,'mobile',keysToSend)
    def send_keys4(self,keysToSend):
        self.send_keys(By.ID,'password',keysToSend)
    def click5(self):
        self.click(By.ID,'regbtn')
    def panduan(self):
        a=self.find_element(By.ID,'rappkey').text
        return a

# A=Api_page(Init_driver())
# A.open1()
# A.click2()
# A.send_keys(By.NAME,'mobile','keysToSend')


