import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_in_site(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_class(".btn.btn-lg.btn-primary.btn-add-to-basket"), "Button not found"
