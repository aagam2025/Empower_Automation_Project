from pages.library_page import library
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_library(page):
    login_page = LoginPage(page)
    dashboard = DashboardPage(page)
    library_pg = library(page)

    login_page.open()
    login_page.login()

    library_pg.go_to_library()
    library_pg.read_library()
    page.go_back()

    dashboard.go_to_dashboard()
    