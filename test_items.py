import pytest
from selenium.webdriver.common.by import By

link_dict = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/',
]

@pytest.mark.parametrize('linkac', link_dict)
def test_shopping_cart_button(browser, linkac):
    link = linkac
    browser.get(link)
    bt = browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert len(bt) == 0, 'button not found'
