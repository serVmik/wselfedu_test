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
