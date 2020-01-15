from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"


def brovser_NAME(search):
    return browser.find_element(By.NAME, f"{search}")


def brovser_ID(search):
    return browser.find_element(By.ID, f"{search}")


try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = brovser_NAME("first_name")
    input1.send_keys("Igor")
    input2 = brovser_NAME("last_name")
    input2.send_keys("Python")
    input3 = brovser_NAME("firstname")
    input3.send_keys("Ua")
    input4 = brovser_ID("country")
    input4.send_keys("Zp")
    brovser_ID("submit_button").click()

finally:
    time.sleep(20)
    browser.quit()