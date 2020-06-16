import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Base_action():
    def __init__(self,driver):
        self.driver=driver
    # 浏览器最大化
    def max_window_size(self):
        self.driver.maximize_window()
    # 设置窗口大小，输入宽和高
    def set_window_size(self,width,height):
        self.driver.set_window_size(width=width,height=height)
    # 打开网址，输入网址
    def open_url(self,url):
        self.driver.get(url=url)
    # 刷新操作
    def refresh(self):
        self.driver.refresh()
    # 前进
    def forward(self):
        self.driver.forward()
    # 后退
    def close(self):
        self.driver.close()
    # 关闭浏览器
    def quit(self):
        self.driver.quit()
    # 找元素，如By.ID,'xxxx'
    def find_element(self,By,value):
        element= WebDriverWait(self.driver,timeout=10,poll_frequency=0.5)\
            .until(lambda x:x.find_element(by=By,value=value))
        return element
    # 找元素组
    def find_elements(self,By,value):
        elements=WebDriverWait(self.driver,timeout=10,poll_frequency=0.5)\
            .until(lambda x:x.find_elements(by=By,value=value))
        return elements
    # 获取cookies
    def get_cookies(self):
        cookies=self.driver.get_cookies()
        return cookies
    # 切换句柄到最新
    def switch_windowHandles(self):
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1:])
    # alert弹出确定
    def switch_alert_accept(self):
        self.driver.switch_to.alert.accept()
    # 弹窗取消
    def switch_alert_dissmiss(self):
        self.driver.switch_to.alert.dismiss()
    # 输入文字
    def switch_alert_send_keys(self,keysToSend):
        self.driver.switch_to.alert.send_keys(keysToSend=keysToSend)
    # 跳到frame或者iframe框架内
    def switch_iframe(self,By,value):
        frame=self.find_element(By=By,value=value)
        self.driver.switch_to.frame(frame)
    # 跳到上一层框架
    def switch_iframe_parent(self):
        self.driver.switch_to.parent_frame()
    # 跳到最开始
    def switch_iframe_default(self):
        self.driver.switch_to.default_content()
    # 点击操作
    def click(self,By,value):
        self.find_element(By=By,value=value).click()
    # 输入文字
    def send_keys(self,By,value,keysToSend):
        self.find_element(By=By,value=value).send_keys(keysToSend)
    # 清楚输入框的内容
    def clear(self,By,value):
        self.find_element(By=By,value=value).clear()
    # 截图保存
    def get_window_screenshot_as_file(self):
        self.driver.get_screenshot_as_file(os.path.abspath('..')+'/'+'data'+'/'+time.strftime('%Y%m%d%H%M%S')+'.png')
    # 删除缓存
    def delete_all_cookies(self):
        self.driver.delete_all_cookies()
    # 滑动屏幕
    def scroll_screen(self,js='window.scrollTo(0,1000)'):
        self.driver.execute_script(js)
    # 悬浮到元素上面
    def move_to_element(self,By,value):
        ActionChains(self.driver).move_to_element(self.find_element(By=By,value=value)).perform()
    # 悬浮到元素组上面
    def move_to_elements(self,By,value):
        ActionChains(self.driver).move_to_element(self.find_elements(By=By,value=value)).perform()
    # 双击
    def double_click(self,By,value):
        ActionChains(self.driver).double_click(self.find_element(By=By,value=value)).perform()
    # 右击
    def context_click(self,By,value):
        ActionChains(self.driver).context_click(self.find_element(By=By,value=value)).perform()
    # 拖动元素到目标元素
    def drag_and_drop(self,By,value,By1,value1):
        ActionChains(self.driver).drag_and_drop(self.find_element(By=By,value=value),self.find_element(By=By1,value=value1)).perform()
    # 隐式等待
    def implictly_wait(self,time):
        self.driver.implicitly_wait(time)
