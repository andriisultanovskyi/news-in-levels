import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Utility to click and wait for URL to load
def click_and_wait_for_url(driver, locator, expected_url_part):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url_part))
    assert expected_url_part in driver.current_url, f"Expected '{expected_url_part}' in {driver.current_url}"

# Scroll and click
def scroll_and_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)
    element.click()

# Parameterized test for levels
@pytest.mark.parametrize("level, expected_url", [
    ("1", "https://www.grammarinlevels.com/level1/"),
    ("2", "https://www.grammarinlevels.com/level2/"),
    ("3", "https://www.grammarinlevels.com/level3/")
])
def test_click_link_levels(grammar, level, expected_url):
    locator = (By.XPATH, f"(//*[text()='Level {level}'])[1]")
    click_and_wait_for_url(grammar, locator, expected_url)

# Test for "Robinson Crusoe"
def test_click_link_robinson_crusoe(grammar, switch_to_new_window):
    element = WebDriverWait(grammar, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Robinson Crusoe']"))
    )
    scroll_and_click(grammar, element)
    switch_to_new_window()
    WebDriverWait(grammar, 10).until(EC.url_contains("robinsoncrusoeinlevels.com"))
    assert "https://www.robinsoncrusoeinlevels.com/" in grammar.current_url

# Test for "Next lesson"
def test_click_button_next_lesson(grammar):
    element = WebDriverWait(grammar, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Next lesson"))
    )
    scroll_and_click(grammar, element)
    WebDriverWait(grammar, 10).until(EC.url_contains("grammarinlevels.com/level1/lesson2/"))
    assert "https://www.grammarinlevels.com/level1/lesson2/" in grammar.current_url
