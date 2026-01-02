# from pages.base_page import BasePage
# from playwright.sync_api import expect

# class CoursesPage(BasePage):
#     # Selectors
#     ADD_COURSE_BUTTON = "#selfAssignment"
#     MODAL = "#selfAssignmentModal"
#     FILTER_DROPDOWN = "#filterwithcategory"
#     CLOSE_BUTTON = "xpath=//*[@id='selfAssignmentModal']/div/div/div[2]/div/div[1]/button"

#     # Course Constants
#     RED_FLAG_COURSE = "RFR - Senior Management"
#     EDUCATION_COURSE = "JCAHO-AIDS(N)"
    
#     DEFAULT_TIMEOUT = 5000

#     def open_add_course_modal(self):
#         """Opens the modal and ensures it is visible."""
#         self.page.locator(self.ADD_COURSE_BUTTON).click()
#         expect(self.page.locator(self.MODAL)).to_be_visible(timeout=self.DEFAULT_TIMEOUT)

#     def filter_by_category(self, category: str):
#         """Selects a category and waits for the UI to update."""
#         dropdown = self.page.locator(self.FILTER_DROPDOWN)
#         # Ensure dropdown is ready before selection
#         # expect(dropdown).to_be_visible(timeout=self.DEFAULT_TIMEOUT)
#         dropdown.select_option(label=category)
#         # Wait for the network to settle as categories usually trigger AJAX calls
#         self.page.wait_for_load_state("networkidle")
#         self.page.wait_for_timeout(2000)

#     def _add_course_if_present(self, course_name: str):
#         course_button = self.page.locator(
#             f'xpath=//*[normalize-space()="{course_name}"]/ancestor::div//button'
#         ).first

#         if course_button.is_visible(timeout=self.DEFAULT_TIMEOUT):
#             course_button.click()
#             print(f"Added course: {course_name}")
#             return True

#         print(f"Course not found: {course_name}")
#         return False
#         # self.page.locator(self.ADD_COURSE_BUTTON).click()
#         """
#         Try to find and click the course button by its ID.
#         Returns True if clicked (added), False if not present or not clickable.
#         """
#         # try:
#         # course_button = self.page.locator(course_name).locator("button").first
#         # if course_button.is_visible():
#         #     course_button.click()
#         #     print(f"Added course: {course_name}")
#         #     return True        
#         # except Exception:
#         #     pass
#         # return False

#     def add_course_redflag_then_education(self) -> bool:
#         """
#         Flow: Filters Red Flags -> Tries to add course. If fails -> Filters Education -> Tries to add course.
#         Returns True if any course was added, False otherwise.
#         """
#         # --- 1. TRY RED FLAGS RULE ---
#         print("Selecting category: Red Flags Rule")
#         self.filter_by_category("Red Flags Rule")
#         if self._add_course_if_present(self.RED_FLAG_COURSE):
#             print(f"Course '{self.RED_FLAG_COURSE}' added successfully.")
#             self.close_modal()
#             return True

#         # --- 2. FALLBACK: EDUCATION ---
#         print(f"'{self.RED_FLAG_COURSE}' not found. Selecting category: Education")
#         self.filter_by_category("Education")

#         if self._add_course_if_present(self.EDUCATION_COURSE):
#             print(f"Course '{self.EDUCATION_COURSE}' added successfully.")
#             self.close_modal()
#             return True

#         # --- 3. FAILURE ---
#         print("Both courses not found or already added.")
#         self.close_modal()
#         return False

#     def close_modal(self):
#         """Scrolls to the bottom of the modal and clicks close."""
#         # modal_selector = "#selfAssignmentModal"
        
#         # # Check if modal is actually open before trying to close it
#         # if self.page.locator(modal_selector).is_visible():
#             # Scroll within the modal element
#         self.page.locator(self.CLOSE_BUTTON).click()
#         expect(self.page.locator(self.MODAL)).to_be_hidden()
            
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
        self.page.wait_for_timeout(1500)  # UI refresh

    # def _assign_course_by_id(self, course_id: str) -> bool:
    #     """
    #     Clicks course button using XPath ID match.
    #     Returns True if clicked, False if not found.
    #     """
    #     try:
    #         course_btn = self.page.locator(
    #             f"xpath=//*[@id={repr(course_id)}]"
    #         )

    #         if course_btn.count() == 0:
    #             return False

    #         expect(course_btn).to_be_visible(timeout=3000)
    #         course_btn.click()
    #         print(f"✅ Assigned course: {course_id}")
    #         return True

    #     except TimeoutError:
    #         return False

    # def add_course_redflag_then_education(self) -> bool:
    #     # 1️⃣ Try Red Flags
    #     print("🔍 Trying Red Flags Rule")
    #     self.filter_by_category("Red Flags Rule")
    #     if self._assign_course_by_id(self.RED_FLAG_ID):
    #         return True

    #     # 2️⃣ Fallback → Education
    #     print("🔁 Red Flag not found, trying Education")
    #     self.filter_by_category("Education")
    #     if self._assign_course_by_id(self.EDUCATION_ID):
    #         return True

    #     # 3️⃣ Nothing found → close modal
    #     print("❌ No course found, closing modal")
    #     self.page.click(self.CLOSE_BUTTON)
    #     return False
    def _assign_course_by_id(self, course_id: str) -> bool:
        try:
            course_btn = self.page.locator(
                f"xpath=//*[@id={repr(course_id)}]"
            )

            if course_btn.count() == 0:
                return False

            course_btn.click()
            print(f"Clicked course: {course_id}")

            # 👉 HANDLE CONFIRM POPUP
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