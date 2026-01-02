from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()

    dashboard = DashboardPage(page)
    dashboard.go_to_dashboard()