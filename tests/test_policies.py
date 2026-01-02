from pages.policies_page import policy
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
def test_policies(page):
    login_page = LoginPage(page)
    policies = policy(page)


    # Login
    login_page.open()
    login_page.login()

    # Verify Policies Page
    policies.go_to_policies()
    policies.read_policies()
    policies.filter_policies()
    policies.filter_policies()
    