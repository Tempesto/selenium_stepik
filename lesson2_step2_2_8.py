import os
from conf import browser

browser.get("http://suninjuly.github.io/file_input.html")
browser.find_element_by_tag_name("[name='firstname']").send_keys("Ig")
browser.find_element_by_tag_name("[name='lastname']").send_keys("Ig")
browser.find_element_by_tag_name("[name='email']").send_keys("Ig@mail.ru")
file_dir = os.path.abspath(os.path.dirname(__file__)) # __file__ означает, что дериктория находится в капке со скриптом
file = os.path.join(file_dir, 'file.txt')
browser.find_element_by_id("file").send_keys(file)
browser.find_element_by_tag_name("button").click()