from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
x_element = browser.find_element_by_xpath("//label/span[2]")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(f"{y}")
browser.find_element_by_css_selector("[for='robotCheckbox']").click()
browser.find_element_by_css_selector("[name='robots']").click()
browser.find_element_by_tag_name("button").click()