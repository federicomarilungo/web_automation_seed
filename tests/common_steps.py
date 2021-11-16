"""
In this module we will put ONLY common steps for ALL or the most of the tests cases
"""

from pages.login import LoginPage

def login(browser, user, password):
    login_page = LoginPage(browser)

    # Given the Backoffice login page is displayed
    login_page.load()

    # When the user logins
    login_page.set_user(user)
    login_page.set_pass(password)
    browser.save_screenshot('./screenshots/login.png')
    login_page.click_get_in()