import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.parametrize("level, menu_text, expected_url_part", [
    ("1", "Exercises", "exercises"),
    ("1", "Funny", "funny"),
    ("1", "History", "history"),
    ("1", "Information", "information"),
    ("1", "Interesting", "interesting"),
    ("1", "Nature", "nature"),
    ("1", "News", "news"),
    ("1", "Sport", "sport"),
    ("2", "Exercises", "exercises"),
    ("2", "Funny", "funny"),
    ("2", "History", "history"),
    ("2", "Information", "information"),
    ("2", "Interesting", "interesting"),
    ("2", "Nature", "nature"),
    ("2", "News", "news"),
    ("2", "Sport", "sport"),
    ("3", "Exercises", "exercises"),
    ("3", "Funny", "funny"),
    ("3", "History", "history"),
    ("3", "Information", "information"),
    ("3", "Interesting", "interesting"),
    ("3", "Nature", "nature"),
    ("3", "News", "news"),
    ("3", "Sport", "sport"),
])


def test_dropdown_menu(browser, level, menu_text, expected_url_part):
    browser.get("https://www.newsinlevels.com/")

    # Hover over "Level X"
    level_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, f"(//*[text()='Level {level}'])[1]"))
    )
    ActionChains(browser).move_to_element(level_element).perform()

    # Wait for the submenu and click
    submenu_link = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, menu_text))
    )
    assert submenu_link.is_displayed(), f"'{menu_text}' submenu not visible"
    submenu_link.click()

    # Check URL
    WebDriverWait(browser, 10).until(EC.url_contains(expected_url_part))
    expected_url = f"https://www.newsinlevels.com/category/{expected_url_part}/?level=level-{level}"
    assert browser.current_url == expected_url, f"Expected URL: {expected_url}, but got: {browser.current_url}"