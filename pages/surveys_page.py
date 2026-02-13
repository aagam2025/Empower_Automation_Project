from conftest import page
from pages.base_page import BasePage

class SurveysPage(BasePage):
    def __init__(self, page):
        self.page = page
        self.surveys_menu = 'xpath=//*[@id="main-menu-navigation"]/li[5]/a/span'
        self.survey_page = None

    def go_to_surveys(self):
        self.page.wait_for_selector(self.surveys_menu)
        self.page.click(self.surveys_menu)
        self.page.wait_for_timeout(8000)

    def survey_start(self):
        with self.page.context.expect_page() as new_page:
            self.page.locator('xpath=//*[@id="main-wrapper"]/div[5]/div[3]/div/div[1]/div/div/form/div/a[1]').first.click()
            # continue_survey_btn = self.page.locator('xpath=//*[@id="main-wrapper"]/div[5]/div[3]/div/div[1]/div/div/form/div/a').first
            # continue_survey_btn.click()
        self.survey_page = new_page.value
        self.survey_page.wait_for_load_state("domcontentloaded")


    def fill_survey(self):
        if self.survey_page is None:
            raise Exception("Survey page is not opened. Did you call survey_start()?")

        page = self.survey_page

        q1 = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/fieldset[4]/label/label')
        if q1.count() > 0 and q1.first.is_visible():
            q1.first.click()
            page.locator('xpath=//*[@id="questions"]/div[2]/div[2]/button').click()

        q2 = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/fieldset[1]/label/label')
        if q2.count() > 0 and q2.first.is_visible():
            q2.first.click()
            page.locator('xpath=//*[@id="questions"]/div[2]/div[2]/button').click()

        q3 = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/div/textarea')
        if q3.count() > 0 and q3.first.is_visible():
            q3.first.fill("This is a test survey response.")
            page.locator('xpath=//*[@id="questions"]/div[2]/div[2]/button').click()

        q4_opt1 = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/fieldset[3]/label/label')
        q4_opt2 = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/fieldset[5]/label/label')
        if q4_opt1.count() > 0 and q4_opt1.first.is_visible():
            q4_opt1.first.click()
            q4_opt2.first.click()
            page.locator('xpath=//*[@id="questions"]/div[2]/div[2]/button').click()

        q5_r1 = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[4]/input')
        if q5_r1.count() > 0 and q5_r1.first.is_visible():
            page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[4]/input').check()
            page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/table/tbody/tr[2]/td[4]/input').check()
            page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/table/tbody/tr[3]/td[4]/input').check()
            page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/table/tbody/tr[4]/td[3]/input').check()
            page.locator('xpath=//*[@id="questions"]/div[2]/div[2]/button').click()

        q6 = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div/div/div/input')
        if q6.count() > 0 and q6.first.is_visible():
            q6.first.wait_for(state="visible")
            q6.first.click()
            q6.first.fill("Test response")

            page.locator('xpath=//*[@id="questions"]/div[2]/div[1]/span/label/span').check()
            page.locator('xpath=//*[@id="questions"]/div[3]/div[2]/button').click()

        print("Survey Completed Successfully.")
