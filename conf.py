from selenium import webdriver

browser = webdriver.Chrome()


def ID(value):
    return browser.find_element_by_id(value)


def TAG(value):
    return browser.find_element_by_tag_name(value)


def GET(value):
    return browser.get(value)