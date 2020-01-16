import unittest
from conf import browser, ID, TAG, GET
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_1(self):
        GET("http://suninjuly.github.io/registration1.html")
        input1 = TAG("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = TAG("[placeholder='Input your last name']")
        input2.send_keys("Sokolov")
        input3 = TAG("[placeholder='Input your email']")
        input3.send_keys("sos@ya.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        welcome_text_elt = TAG("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Тест '1' не прошел")

    def test_2(self):
        GET("http://suninjuly.github.io/registration2.html")
        input1 = TAG("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = TAG("[placeholder='Input your last name']")
        input2.send_keys("Sokolov")
        input3 = TAG("[placeholder='Input your email']")
        input3.send_keys("sos@ya.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Тест '2' не прошел")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")