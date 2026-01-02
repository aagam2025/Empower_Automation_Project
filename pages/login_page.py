from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):

    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password-field"
    LOGIN_BUTTON = "#empower_btn_submit"

    def open(self):
        self.page.goto(Config.BASE_URL, timeout=60000)
        self.wait_for_network()

    def login(self):
        self.fill(self.EMAIL_INPUT, Config.USERNAME)
        self.fill(self.PASSWORD_INPUT, Config.PASSWORD)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_network()
