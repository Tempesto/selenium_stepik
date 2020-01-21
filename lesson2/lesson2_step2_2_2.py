from conf import browser
from selenium.webdriver.support.ui import Select

browser.get("http://suninjuly.github.io/selects1.html")
select =Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1")

# Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). Первый
# способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего
# примера.

# Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля. Для того чтобы найти
# элемент с текстом "Python", нужно использовать select.select_by_index(1), так как опция с индексом 0 в данном примере
# имеет значение по умолчанию равное "--".