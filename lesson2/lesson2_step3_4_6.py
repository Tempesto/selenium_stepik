from conf import browser, ID, TAG, GET
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


GET("http://suninjuly.github.io/redirect_accept.html")
TAG("button").click()
win2 = browser.window_handles[1] # записываем название второго окна
browser.switch_to_window(win2) # переключаемся на второе окно
num = ID("input_value").text
print("num = ", num)
sum = calc(num)
ID("answer").send_keys(sum)
TAG("button").click()