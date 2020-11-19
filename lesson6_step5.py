from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link2 = browser.find_element_by_link_text(a)
    link2.click()
    input1 = browser.find_element_by_css_selector("form>.form-group:nth-child(1)>input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()