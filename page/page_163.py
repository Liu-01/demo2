from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_action import Base_action


class Page_163(Base_action):
    def open1(self):
        self.open_url('E:/下载/163.html')
    def switch_iframe2(self):
        self.switch_iframe(By.CSS_SELECTOR,'iframe[id^="x-URS-iframe"]')
    def send_keys3(self,name):
        self.send_keys(By.NAME,'email',keysToSend=name)
    def send_keys4(self,password):
        self.send_keys(By.NAME,'password',password)

    # 扫码登录id:wloginErrorBox__ScanCodeBtn