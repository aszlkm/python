from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
browser=webdriver.Chrome("D:\\python\\chromedriver.exe")
browser.implicitly_wait(7)
phonenumber="xxxxxxx"
browser.get('https://login.10086.cn/login.html?channelID=12034&backUrl=http%3A%2F%2Fwww.10086.cn%2Findex%2Fxz%2Findex_891_897.html')
browser.find_element_by_xpath('//*[@id="sms_login_1"]').click()
browser.find_element_by_xpath('//*[@id="sms_name"]').click()
browser.find_element_by_xpath('//*[@id="sms_name"]').send_keys(phonenumber)
browser.find_element_by_xpath('//*[@id="getSMSPwd1"]').click()
#广百会
browser.get('http://wap.gbhui.com/captcha_login.html')
browser.find_element_by_xpath('//*[@id="loginName"]').click()
browser.find_element_by_xpath('//*[@id="loginName"]').send_keys(phonenumber)
browser.find_element_by_xpath('//*[@id="btnSendCode"]').click()
#庇荫及时
browser.get('https://www.biyinjishi.com/MUCenter/Home/UserRegister?rUrl=https://www.biyinjishi.com/mf/index')
browser.find_element_by_xpath('//*[@id="phone"]').click()
browser.find_element_by_xpath('//*[@id="phone"]').send_keys(phonenumber)
browser.find_element_by_xpath('//*[@id="butsendVCode4Phone"]').click()
# 2car
x=1
for x in range(10):
    browser.get('https://2car.haval.com.cn/quicklogin')
    # browser.find_element_by_xpath('//*[@id="phone"]').click()
    browser.find_element_by_xpath('//*[@id="phone"]').send_keys(phonenumber)
    ele=browser.find_element_by_xpath("/html/body/div/div/div/form/ul/li[2]/a")
    ele.click()
    time.sleep(20) 
# 米哈由
for x in range(10):
    browser.get('https://user.mihoyo.com/#/register/mobile?cb_route=%2Faccount%2Fhome')
    # browser.find_element_by_xpath('//*[@id="phone"]').click()
    browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[1]/div/input').send_keys(phonenumber)
    ele=browser.find_element_by_xpath(" //div[@class='input-inner-btn']")
    ele.click()
    time.sleep(20)
#乐业天空
for x in range(10):
    browser.get('http://www.myjobsky.com/Account/Register')
    # browser.find_element_by_xpath('//*[@id="phone"]').click()
    browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[1]/div/input').send_keys(phonenumber)
    ele=browser.find_element_by_xpath(" //div[@class='input-inner-btn']")
    ele.click()
    time.sleep(20)
# print(ele)
# browser.find_element_by_xpath('//*[@id="ConfirmPassword"]').click()
# browser.find_element_by_xpath('//*[@id="ConfirmPassword"]').send_keys('pwd123456')
# browser.find_element_by_xpath('//*[@id="chkCodeSendBtn"]').click()

# for i in range(50):
#     driver.find_element_by_xpath('//*[@id="send-number-button"]').click()
#     print (i)
#     time.sleep(63)