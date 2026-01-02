# https://develop.empowerlms.com/register using this link i want to signup new user
from config.config import Config
from pages.base_page import BasePage
from playwright.sync_api import expect
class SignupPage(BasePage):
    # Selectors
    EMAIL_INPUT = "#email"
    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    SIGNUP_BUTTON = "#hsh_btn_submit"
    SUCCESS_MESSAGE = "text=Registration successful"

    def open(self):
        """Navigate to the signup page."""
        self.page.goto(Config.SIGNUP_URL)

    def signup(self):
        """Fill out the signup form and submit."""
        self.page.fill(self.EMAIL_INPUT, Config.EMAIL)
        self.page.fill(self.FIRST_NAME_INPUT, Config.FIRST_NAME)
        self.page.fill(self.LAST_NAME_INPUT, Config.LAST_NAME)
        self.page.click(self.SIGNUP_BUTTON)