from pages.signup_page import SignupPage

def test_add_user(page):
    signupage = SignupPage(page)
    signupage.open()
    signupage.signup()