from conf import browser
from selenium.webdriver.support.ui import Select

browser.get("http://suninjuly.github.io/selects2.html")
num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text
sum = int(num1) + int(num2)
print("num1 = ", num1)
print("num2 = ", num2)
print("sum = ", sum)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(f"{sum}")
browser.find_element_by_tag_name("button").click()