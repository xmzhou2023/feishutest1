import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
import webbrowser
from selenium.webdriver.common.by import By


# 打开浏览器
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 去掉自动化监控
browser = webdriver.Chrome(options=options)  # 打开浏览器
browser.maximize_window()  # 浏览器最大化
browser.get('https://www.feishu.cn/')  # 输入链接
time.sleep(20)

browser.find_element(By.XPATH, "//a[normalize-space(text())='登录']").click() # 登录
browser.find_element(By.XPATH, "//input[@id='account']").click()  # 用户名
browser.find_element(By.XPATH, "//input[@id='account']").send_keys('test1')
time.sleep(1)
browser.find_element(By.XPATH, "//input[@id='password']").click()  # 密码
browser.find_element(By.XPATH, "//input[@id='password']").send_keys('itelsimson2022.')
browser.find_element(By.XPATH, "//button[@data-spm='home_next']").click()  # login
time.sleep(5)
browser.find_element(By.XPATH, "//div[@class='_pp-product-container']").click() # 点击九点
time.sleep(2)
browser.find_element(By.XPATH, "//div[@title='消息']").click()  # 进入消息页面
time.sleep(5)
browser.find_element(By.XPATH, "//p[normalize-space(text())='test2']").click()  # 找到test2联系人
browser.find_element(By.XPATH, "//pre[@data-text='发送给 test2']").click()
browser.find_element(By.XPATH, "//pre[@data-text='发送给 test2']").send_keys('itelsimson2022.') # 输入消息
time.sleep(2)
pyautogui.press('Enter')  # 按Enter键发送消息


