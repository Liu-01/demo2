import time
import unittest

from ddt import ddt
from selenium import webdriver

from base.base_action import Base_action


@ddt
class PageBaidu(unittest.TestCase):
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
    def baidu_search(self, search_key):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
