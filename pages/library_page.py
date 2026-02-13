from pages.base_page import BasePage

class library(BasePage):
    def __init__(self, page):
        self.page = page
        self.library_btn = "xpath=//*[@id='main-menu-navigation']/li[4]/a"
        self.read_library_btn = "xpath=//*[@id='readResignBtnDiv-22']/a"

    def go_to_library(self):
        self.page.wait_for_selector(self.library_btn)
        self.page.click(self.library_btn)
        self.page.wait_for_timeout(8000)
    
    def read_library(self):
        self.page.wait_for_selector(self.read_library_btn)
        self.page.click(self.read_library_btn)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

        for _ in range(15):
            self.page.mouse.wheel(0, 200)
            self.page.wait_for_timeout(1500)
