import time
import pytest
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_find_basket(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements_by_css_selector('#add_to_basket_form .btn-add-to-basket')
if __name__ == '__main__':
    pytest.main()