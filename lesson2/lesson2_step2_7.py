from conf import browser
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser.get("http://suninjuly.github.io/get_attribute.html")
img1 = browser.find_element_by_tag_name("img")
img1_value_atribute = img1.get_attribute("valuex")
res = calc(img1_value_atribute)
browser.find_element_by_id("answer").send_keys(f"{res}")
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_css_selector("[value='robots']").click()
browser.find_element_by_tag_name("button").click()