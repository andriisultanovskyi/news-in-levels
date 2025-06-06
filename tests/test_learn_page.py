import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def click_and_wait_for_url(driver, locator, expected_url_part):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url_part))
    assert expected_url_part in driver.current_url


def scroll_and_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)
    element.click()

# Parameterized test for levels
@pytest.mark.parametrize("level, expected_url", [
    ("1", "https://www.howtolearnenglishinlevels.com/level1/"),
    ("2", "https://www.howtolearnenglishinlevels.com/level2/"),
    ("3", "https://www.howtolearnenglishinlevels.com/level3/")
])
def test_click_link_levels(learn, level, expected_url):
    locator = (By.XPATH, f"(//*[text()='Level {level}'])[1]")
    click_and_wait_for_url(learn, locator, expected_url)

# Test "Next lesson"
def test_click_button_next_lesson(learn):
    button = WebDriverWait(learn, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Next lesson"))
    )
    scroll_and_click(learn, button)
    expected_url = "https://www.howtolearnenglishinlevels.com/level1/lesson2/"
    WebDriverWait(learn, 10).until(EC.url_contains("level1/lesson2"))
    assert expected_url in learn.current_url

# Test Twitter
def test_click_icon_twitter(learn):
    icon = WebDriverWait(learn, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="http://twitter.com/newsinlevels"]'))
    )
    scroll_and_click(learn, icon)
    WebDriverWait(learn, 10).until(EC.url_contains("x.com/newsinlevels"))
    assert "https://x.com/newsinlevels" in learn.current_url

