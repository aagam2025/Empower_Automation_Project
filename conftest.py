import pytest
from playwright.sync_api import sync_playwright
from config.config import Config


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        context = browser.new_context()
        # context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        yield page
        # context.tracing.stop(path="trace.zip")
        # context.close()
        browser.close()
