from selenium import webdriver
import sys

def is_driver(no_ui=False):
    ''' 1、判断是在什么环境下运行
        2、no_ui win系统下默认为界面模式，无界面设为：True
    '''
    if 'linux' in sys.platform:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')                 # 浏览器不提供可视化页面
        option.add_argument('no-sandbox')               # 以最高权限运行
        option.add_argument('--start-maximized')        # 最大化运行（全屏窗口）设置元素定位比较准确
        option.add_argument('--disable-gpu')            # 谷歌文档提到需要加上这个属性来规避bug
        # option.add_argument('--window-size=1920,1080')  # 设置浏览器分辨率（窗口大小）
        driver = webdriver.Chrome(options=option)
    else:
        if no_ui:
            ''' win系统下无界面模式 '''
            option = webdriver.ChromeOptions()
            option.add_argument('headless')             # 浏览器不提供可视化页面
            option.add_argument('--start-maximized')    # 最大化运行（全屏窗口）设置元素定位比较准确
            driver = webdriver.Chrome(chrome_options=option)
        # else:
        #     driver = webdriver.Chrome()
        #     driver.maximize_window()                    # 将浏览器最大化
    return driver
driver = is_driver()
driver.get('https://www.baidu.com/')
print('title：', driver.title)
print('执行完毕：！！！')
driver.quit()
