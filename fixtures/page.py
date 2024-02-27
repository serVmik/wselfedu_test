import pytest
from playwright.sync_api import Page, sync_playwright, Browser, BrowserContext

HEADLESS = False
SLOW_MO = 3000


@pytest.fixture(scope='class')
def new_page() -> Page:
    p = sync_playwright().start()
    browser: Browser = p.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO,
    )
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    yield page
    for context in browser.contexts:
        context.close()
    browser.close()
    p.stop()
