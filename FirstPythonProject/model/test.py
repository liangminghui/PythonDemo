# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
'''
    更新插件
    python -m pip install --upgrade pip
    安装 selenium
    pip install selenium
'''

# 凡是出现sleep的，都是因为网络等原因加载过慢，需要等一等

# 登录云盘
def login(driver,username,password):
    orgin_url = 'https://pan.baidu.com/'
    driver.get(orgin_url)
    time.sleep(5)
    elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    elem_static.click()
    time.sleep(0.5)
    elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    elem_username.clear()
    elem_username.send_keys(username)
    elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    elem_userpas.clear()
    elem_userpas.send_keys(password)
    elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    elem_submit.click()
    time.sleep(5)
# 将加密分享的文件保存到自己云盘的目录下[AA]
def extract(driver,srcurl,srcpwd):
    driver.get(srcurl)
    try:
        getpwd = driver.find_element_by_id("esDEV5")
        getpwd.send_keys(srcpwd)
        getButton = driver.find_element_by_link_text("提取文件")
        getButton.click()
        time.sleep(10)
        # 目前有两种情况
        # 一：分享文件是一压缩包
        # 二：分享的是一路径
        try:
            # 全选（情况二）
            selectall = driver.find_element_by_class_name("zbyDdwb")
            selectall.click()
        except NoSuchElementException:
            file_name = "no_zbyDdwb.png"
            driver.save_screenshot(file_name)
            driver.get_screenshot_as_file(file_name)
            pass
        savetodisk = driver.find_element_by_link_text("保存到网盘")
        savetodisk.click()
        time.sleep(5)
        # AA 保存路径
        selectdir = driver.find_element_by_xpath("//span[@node-path='/AA']")
        selectdir.click()
        enter = driver.find_element_by_link_text("确定")
        enter.click()
        time.sleep(2)
    except NoSuchElementException:
        file_name = "no_such_element.png"
        driver.get_screenshot_as_file(file_name)
        pass


def doWork():
    driver = webdriver.Chrome()
    #login(driver,"15053168633","LMH19951007")
    extract(driver, "https://pan.baidu.com/s/1SuwOoa54XMQHUfhRR2d8MA", "9ing")
    driver.quit()
if __name__ == '__main__':
    doWork()
