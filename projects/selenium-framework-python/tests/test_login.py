
from pages.login_page import LoginPage

def test_login_flow(driver):
    page = LoginPage(driver)
    page.load("https://the-internet.herokuapp.com/login")
    page.login("tomsmith", "SuperSecretPassword!")
    assert "secure" in driver.current_url
