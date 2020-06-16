from selenium import webdriver

def Init_driver(name=None):
    global driver
    if name=='ie':
        driver=webdriver.Ie()
    elif name=='firefox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver