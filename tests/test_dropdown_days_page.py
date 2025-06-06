import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.parametrize("level, menu_text, expected_url_part", [
    ("1", "21st century", "21-century"),
    ("1", "Crime", "crime"),
    ("1", "Disasters", "disasters"),
    ("1", "Exploration", "exploration"),
    ("1", "Landmarks", "landmarks"),
    ("1", "Science", "science"),
    ("1", "War", "war"),
    ("2", "21st century", "21-century"),
    ("2", "Crime", "crime"),
    ("2", "Disasters", "disasters"),
    ("2", "Exploration", "exploration"),
    ("2", "Landmarks", "landmarks"),
    ("2", "Science", "science"),
    ("2", "War", "war"),
    ("3", "21st century", "21-century"),
    ("3", "Crime", "crime"),
    ("3", "Disasters", "disasters"),
    ("3", "Exploration", "exploration"),
    ("3", "Landmarks", "landmarks"),
    ("3", "Science", "science"),
    ("3", "War", "war"),
])
def test_dropdown_menu(driver, level, menu_text, expected_url_part):
    driver.get("https://www.daysinlevels.com/?utm_source=NiLMenu")

    # Hover over "Level X"
    level_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"(//*[text()='Level {level}'])[1]"))
    )
    ActionChains(driver).move_to_element(level_element).perform()

    # Wait for the submenu and click
    submenu_link = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, menu_text))
    )
    assert submenu_link.is_displayed(), f"'{menu_text}' submenu not visible"
    submenu_link.click()

    # Check URL
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url_part))
    expected_url = f"https://www.daysinlevels.com/category/{expected_url_part}/?level=level-{level}"
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, but got: {driver.current_url}"

