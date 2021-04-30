from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_in_basket_on_localization(browser):
     browser.get(link)
     try:
         button=browser.find_element_by_css_selector("form.add-to-basket button.btn")
         element_present=True
     except Exception:
         element_present=False
     assert element_present, "Button add to basket not present"

