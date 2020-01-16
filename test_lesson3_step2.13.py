import unittest
from conf import browser, ID, TAG, GET
import time


class TestRegistration(unittest.TestCase):
    def test_1(self):
        GET("http://suninjuly.github.io/registration1.html")


        # Ваш код, который заполняет обязательные поля
        input1 = TAG("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = TAG("[placeholder='Input your last name']")
        input2.send_keys("Sokolov")
        input3 = TAG("[placeholder='Input your email']")
        input3.send_keys("sos@ya.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = TAG("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Тест '1' не прошел")

    def test_2(self):
        GET("http://suninjuly.github.io/registration2.html")


        # Ваш код, который заполняет обязательные поля
        input1 = TAG("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = TAG("[placeholder='Input your last name']")
        input2.send_keys("Sokolov")
        input3 = TAG("[placeholder='Input your email']")
        input3.send_keys("sos@ya.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Тест '2' не прошел")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")