import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    #Given I am on OrangeHRM login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #When I login with Valid Credentials
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    #Then i should see the Homepage of OrangeHRM with title Dashboard
    expect(page.get_by_label("Sidepanel").get_by_role("list")).to_contain_text("Dashboard")


# Given, When, Then(BDD)