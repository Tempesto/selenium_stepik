from conf import browser
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.get("http://suninjuly.github.io/execute_script.html")
x = browser.find_element_by_id("input_value").text
res = calc(x)
browser.find_element_by_id("answer").send_keys(res)
browser.find_element_by_id("robotCheckbox").click()
radio_button = browser.find_element_by_tag_name("[value = 'robots']")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
radio_button.click()
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()