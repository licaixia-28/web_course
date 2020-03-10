# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/10

E-mail:530103946@qq.com

=================================


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# 打开浏览器，访问网址
driver = webdriver.Chrome()
# driver.maximize_window()

driver.get("https://www.baidu.com")

loc = By.XPATH, "//input[@id='kw']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("Python")

loc = By.XPATH, "//input[@id='su']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(8)

# driver.quit()
driver.close()


