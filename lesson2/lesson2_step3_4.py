from conf import browser, ID, TAG
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser.get("http://suninjuly.github.io/alert_accept.html")
TAG("button").click()
alert_ok = browser.switch_to_alert() # свитчимся на алерт
alert_ok.accept() # в алерте жмем кнопку согласия
num = ID("input_value").text
res = calc(num)
ID("answer").send_keys(res)
TAG("button").click()