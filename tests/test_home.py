import re

from playwright.sync_api import expect, sync_playwright

BASE_URL = 'http://d45400kr.beget.tech'
STATE_PATH = './tests/.auth/state.json'

HEADLESS = False
SLOW_MO = 4000


def test_home():
    p = sync_playwright().start()
    browser = p.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO,
    )
    context = browser.new_context(storage_state=STATE_PATH)
    page = context.new_page()
    page.goto(BASE_URL)

    expect(page).to_have_title(re.compile('WSE: Домашняя страница'))
    expect(page.get_by_role('link', name='Выйти')).to_be_visible()

    for context in browser.contexts:
        context.close()
    browser.close()
    p.stop()
