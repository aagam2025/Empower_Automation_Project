from pages.base_page import BasePage
from playwright.sync_api import expect, TimeoutError
class CoursesPage(BasePage):
    ADD_COURSE_BUTTON = "#selfAssignment"
    MODAL = "#selfAssignmentModal"
    FILTER_DROPDOWN = "#filterwithcategory"
    CLOSE_BUTTON = "xpath=//*[@id='selfAssignmentModal']//button[contains(.,'Close')]"

    RED_FLAG_ID = "RFR - Senior Management"
    EDUCATION_ID = "JCAHO-AIDS(N)"
    CONFIRM_BUTTON = "xpath=/html/body/div[5]/div/div[4]/div[2]/button"

    def open_add_course_modal(self):
        self.page.click(self.ADD_COURSE_BUTTON)
        expect(self.page.locator(self.MODAL)).to_be_visible()

    def filter_by_category(self, category: str):
        self.page.select_option(self.FILTER_DROPDOWN, label=category)
        self.page.wait_for_timeout(1500)
    def _assign_course_by_id(self, course_id: str) -> bool:
        try:
            course_btn = self.page.locator(
                f"xpath=//*[@id={repr(course_id)}]"
            )

            if course_btn.count() == 0:
                return False

            course_btn.click()
            print(f"Clicked course: {course_id}")
            confirm_btn = self.page.locator(self.CONFIRM_BUTTON)
            expect(confirm_btn).to_be_visible(timeout=5000)
            confirm_btn.click()
            print("Confirmed course assignment")
            return True
        except TimeoutError:
            return False
    def add_course_redflag_then_education(self) -> bool:
        print("Trying Red Flags Rule")
        self.filter_by_category("Red Flags Rule")
        if self._assign_course_by_id(self.RED_FLAG_ID):
            return True
        print("Red Flag not found, trying Education")
        self.filter_by_category("Education")
        if self._assign_course_by_id(self.EDUCATION_ID):
            return True
        print("No course found, closing modal")
        self.page.click(self.CLOSE_BUTTON)
        return False
