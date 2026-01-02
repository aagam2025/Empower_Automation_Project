from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_MENU = "xpath=//*[@id='main-menu-navigation']/li[1]/a/span"
    COURSES_MENU = "xpath=//*[@id='main-menu-navigation']/li[2]/a/span"
    POLICIES_MENU = "xpath=//*[@id='main-menu-navigation']/li[3]/a"
    LIBRARY_MENU = "xpath=//*[@id='main-menu-navigation']/li[4]/a"
    SURVEYS_MENU = "xpath=//*[@id='main-menu-navigation']/li[5]/a"
    GROUPASSIGNMENTS_MENU = "xpath=//*[@id='main-menu-navigation']/li[6]/a"

    def go_to_dashboard(self):
        self.click(self.DASHBOARD_MENU)
        self.page.wait_for_url("**/dashboard**", timeout=10000)

    def go_to_courses(self):
        self.force_click(self.COURSES_MENU)
        self.wait_for_network()

    def go_to_policypage(self):
        self.click(self.POLICIES_MENU)
        self.wait_for_network()

    def go_to_librarypage(self):
        self.click(self.LIBRARY_MENU)
        self.wait_for_network()

    def go_to_surveyspage(self):
        self.click(self.SURVEYS_MENU)
        self.wait_for_network()
    
    def go_to_groupassignments(self):
        self.click(self.GROUPASSIGNMENTS_MENU)
        self.wait_for_network()