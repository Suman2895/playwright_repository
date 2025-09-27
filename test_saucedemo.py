import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    # Arrange:
    page.goto("https://www.saucedemo.com/")

    # Act:
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert:
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")

# AAA Structure(Arrange, Act, Assert)