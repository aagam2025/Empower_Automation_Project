from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_dashboardpage(page):
    dashboard = DashboardPage(page)

    loginpg = LoginPage(page)
    loginpg.open()
    loginpg.login()

    dashboard.go_to_dashboard()
    dashboard.go_to_courses()
    page.go_back()
    dashboard.go_to_policypage()
    page.go_back()
    dashboard.go_to_librarypage()
    page.go_back()
    dashboard.go_to_surveyspage()
    page.go_back()
    dashboard.go_to_groupassignments()
    page.go_back()