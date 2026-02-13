from pages.base_page import BasePage

class policy(BasePage):
    def __init__(self, page):
        self.page = page
        self.policies = 'xpath=//*[@id="main-menu-navigation"]/li[3]/a/span'

    def go_to_policies(self):
        self.page.wait_for_selector(self.policies)
        self.page.click(self.policies)
        self.page.wait_for_timeout(8000)

    def read_policies(self):
        policy_1 = self.page.locator('xpath=//*[@id="readResignBtnDiv-61"]/a').first
        
        with self.page.context.expect_page() as pdf_page_info:
            policy_1.click()

        pdf_page = pdf_page_info.value
        
        pdf_page.wait_for_load_state("load")
        pdf_page.wait_for_timeout(8000)
        pdf_page.close()

        self.page.wait_for_timeout(1000)

    def filter_policies(self):
        filter_checkbox = self.page.locator('xpath=//*[@id="policieslistContainer"]/div/div[1]/div/div/div/div[2]/fieldset/div')
        filter_checkbox.click()
        self.page.wait_for_timeout(5000)
