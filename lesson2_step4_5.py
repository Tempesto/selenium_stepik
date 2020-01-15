from conf import browser, ID


# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = ID("verify").click()
message = ID("verify_message").text

assert "successful" in message