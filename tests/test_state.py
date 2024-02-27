import pytest
from playwright.sync_api import expect, Page

BASE_URL = 'http://d45400kr.beget.tech'
STATE_PATH = './tests/.auth/state.json'


@pytest.mark.browser_context_args(storage_state=STATE_PATH)
def test_state(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role('link', name='ВыЙтИ')).to_be_visible()
