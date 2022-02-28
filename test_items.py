import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_of_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_css_selector(".btn-add-to-basket").is_displayed(), \
        "Button is not displayed!"
