from pages.base import MainPage

BASE_URL = 'http://d45400kr.beget.tech'
TITLE = 'WSE: Домашняя страница'


class TestHome:
    def test_home(self, new_page):
        p = MainPage(new_page)
        p.go_to(BASE_URL)
        p.check_title(TITLE)
