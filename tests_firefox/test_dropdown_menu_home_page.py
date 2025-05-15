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



def test_hover_dropdown_level_1_days(driver):
    hover_dropdown_level_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(hover_dropdown_level_1).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, '21st century')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"


def test_dropdown_menu_l_1_21st_century(driver):
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    dropdown_menu_l_1_21st_century = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown_menu_l_1_21st_century).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, '21st century')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"
    dropdown.click()
    WebDriverWait(driver, 10).until(EC.url_contains("21-century"))
    assert "https://www.daysinlevels.com/category/21-century/?level=level-1" in driver.current_url


def test_dropdown_menu_l_1_crime(driver):
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    dropdown_menu_l_1_crime = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown_menu_l_1_crime).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Crime')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"
    dropdown.click()
    WebDriverWait(driver, 10).until(EC.url_contains("crime"))
    assert "https://www.daysinlevels.com/category/crime/?level=level-1" in driver.current_url


def test_dropdown_menu_l_1_disasters(driver):
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    dropdown_menu_l_1_disasters = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown_menu_l_1_disasters).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Disasters')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"
    dropdown.click()
    WebDriverWait(driver, 10).until(EC.url_contains("disasters"))
    assert "https://www.daysinlevels.com/category/disasters/?level=level-1" in driver.current_url


def test_dropdown_menu_l_1_exploration(driver):
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    dropdown_menu_l_1_exploration = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown_menu_l_1_exploration).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Exploration')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"
    dropdown.click()
    WebDriverWait(driver, 10).until(EC.url_contains("exploration"))
    assert "https://www.daysinlevels.com/category/exploration/?level=level-1" in driver.current_url


def test_dropdown_menu_l_1_landmarks(driver):
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    dropdown_menu_l_1_landmarks = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown_menu_l_1_landmarks).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Landmarks')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"
    dropdown.click()
    WebDriverWait(driver, 10).until(EC.url_contains("landmarks"))
    assert "https://www.daysinlevels.com/category/landmarks/?level=level-1" in driver.current_url


def test_dropdown_menu_l_1_science(driver):
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    dropdown_menu_l_1_science = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown_menu_l_1_science).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Science')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"
    dropdown.click()
    WebDriverWait(driver, 10).until(EC.url_contains("science"))
    assert "https://www.daysinlevels.com/category/science/?level=level-1" in driver.current_url


def test_dropdown_menu_l_1_war(driver):
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    dropdown_menu_l_1_war = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Level 1'][1]")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown_menu_l_1_war).perform()
    dropdown = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'War')))
    assert dropdown.is_displayed(), "The drop down menu did not appear"
    dropdown.click()
    WebDriverWait(driver, 10).until(EC.url_contains("war"))
    assert "https://www.daysinlevels.com/category/war/?level=level-1" in driver.current_url
