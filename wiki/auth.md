test_auth.py
```cfgrlanguage
import os
from urllib.parse import urljoin

from dotenv import load_dotenv
from playwright.sync_api import expect, sync_playwright

load_dotenv()


BASE_URL = 'http://d45400kr.beget.tech'
AUTH_PATH = 'users/login/'
USER_NAME = os.getenv('USER_NAME')
USER_PASSWORD = os.getenv('USER_PASSWORD')
STATE_PATH = './tests/.auth/state.json'

HEADLESS = False
SLOW_MO = 2000


def test_auth():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO,
        )
        context = browser.new_context()
        page = context.new_page()
        page.goto(urljoin(BASE_URL, AUTH_PATH))

        expect(page.get_by_text('Вход в приложение')).to_be_visible()

        page.get_by_placeholder('Имя пользователя').fill(USER_NAME)
        page.get_by_placeholder('Пароль').fill(USER_PASSWORD)
        page.get_by_role('button', name='Войти').click()

        context.storage_state(path=STATE_PATH)
```