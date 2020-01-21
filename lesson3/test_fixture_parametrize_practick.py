import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# @pytest.mark.parametrize('id', ["236895"])
def test_com(id, browser, ):
    link = f"https://stepik.org/lesson/{id}/step/1"
    answer = math.log(int(time.time()))
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//div/textarea"))#проверяем
    # появилсяли элемент на страничке
    text = browser.find_element_by_xpath("//div/textarea")
    text.send_keys(str(answer))
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission")))
    browser.find_element_by_class_name("submit-submission").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    res = browser.find_element_by_xpath("//div/pre").text
    assert res == "Correct!"
