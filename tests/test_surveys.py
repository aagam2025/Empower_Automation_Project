from pages.surveys_page import SurveysPage
from pages.login_page import LoginPage

def test_surveys(page):
    login_page = LoginPage(page)
    # dashboard = DashboardPage(page)
    surveys = SurveysPage(page)

    # Login
    login_page.open()
    login_page.login()

    # dashboard.go_to_dashboard()
    
    # Verify Surveys Page
    surveys.go_to_surveys()
    surveys.survey_start()
    surveys.fill_survey()