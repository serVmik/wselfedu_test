./fixtures/page.py
```cfgrlanguage
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
```

./pages/base.py  
```cfgrlanguage
from playwright.sync_api import expect, Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page


class PageAction:

    page: Page

    def go_to(self, url: str):
        self.page.goto(url)


class CheckPage:

    page: Page

    def check_title(self, title_name: str):
        expect(self.page).to_have_title(title_name)


class MainPage(BasePage, PageAction, CheckPage):
    pass
```

./tests/test_page.py
```cfgrlanguage
from pages.base import MainPage

BASE_URL = 'http://d45400kr.beget.tech'
TITLE = 'WSE: Домашняя страница'


class TestHome:
    def test_home(self, new_page):
        p = MainPage(new_page)
        p.go_to(BASE_URL)
        p.check_title(TITLE)
```