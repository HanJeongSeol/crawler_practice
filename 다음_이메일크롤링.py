from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe")

options = webdriver.ChromeOptions()
# options.add_argument('headless')
browser = webdriver.Chrome('chromedriver',chrome_options=options)

browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")


id = browser.find_element_by_css_selector('input#id')
id.send_keys("ID")

pw = browser.find_element_by_css_selector('input#inputPwd')
pw.send_keys("PW")

browser.find_element_by_css_selector('button#loginBtn').click()
time.sleep(3)

browser.get("https://mail.daum.net/")
time.sleep(3)

title = browser.find_elements_by_css_selector("strong.tit_subject")

for i in title:
    print(i.text)