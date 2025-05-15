import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def wait_and_switch_to_new_window(driver):
    """Waits for a new window to open and switches to it"""
    def _switch():
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        windows = driver.window_handles
        print(f"Open windows: {windows}")
        if len(windows) > 1:
            driver.switch_to.window(windows[1])
        else:
            pytest.fail("New window did not open")
    return _switch


def click_and_verify(driver, locator, expected_url, wait_for_new_window=False):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()
    if wait_for_new_window:
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url))
    assert expected_url in driver.current_url, f"Unexpected URL: {driver.current_url}"


# The test checks the click of the "Home" button on the header and goes to the "Days in levels" page
def test_click_button_home(driver):
    click_button_home = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'mainhome'))
    )
    click_button_home.click()
    WebDriverWait(driver, 10).until(EC.url_contains("daysinlevels.com"))
    assert "https://www.daysinlevels.com/" in driver.current_url


# The test checks the click of the "Test" button on the header and goes to the test page
def test_click_button_test(driver):
    click_and_verify(
        driver,
        (By.XPATH, '//a[@href="https://www.testlanguages.com/?utm_source=DiLMenu"]'),
        "testlanguages.com",
        wait_for_new_window=True
    )


# The test checks the click of the "News" button on the header and goes to the news page
def test_click_button_news(driver):
    click_and_verify(
        driver,
        (By.XPATH, '//a[@href="https://www.newsinlevels.com/?utm_source=DiLMenu"]'),
        "newsinlevels.com",
        wait_for_new_window=True
    )


# The tests check for news of the day, clicks the button 'Level 1, 2, 3' and go to the page of this news
@pytest.mark.parametrize("level", ["1", "2", "3"])
def test_click_level_nav_button(driver, level):
    xpath = (
        f"//li[contains(@class, 'taxonomy') and contains(@class, 'dropdown')]"
        f"//a[contains(@href, '/level/level-{level}/') and text()='Level {level}']"
    )

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    button.click()

    # Checking the transition to the page of the required level
    expected_url_part = f"/level/level-{level}/"
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url_part))
    assert expected_url_part in driver.current_url, f"Unexpected URL: {driver.current_url}"


# The test checks the click of the "Languages" Link and goes to the test page
def test_click_link_test_languages(driver):
    click_and_verify(
        driver,
        (By.LINK_TEXT, 'Test Languages'),
        "testlanguages.com",
        wait_for_new_window=True
    )


# The test checks the click of the "Skype section" Link and goes to the speak in levels page
def test_click_link_skype_section(driver):
    click_and_verify(
        driver,
        (By.LINK_TEXT, 'Skype section'),
        "speakinlevels.com",
        wait_for_new_window=True
    )


# The test checks the click of the "Speak in levels" Link and goes to the speak in levels page
def test_click_link_speak_in_levels(driver):
    click_and_verify(
        driver,
        (By.LINK_TEXT, 'Speak in Levels'),
        "speakinlevels.com",
        wait_for_new_window=True
    )


# The test checks the click of the "YouTube" icon and goes to the days in levels YouTube page
def test_click_icon_youtube(driver):
    click_and_verify(
        driver,
        (By.CLASS_NAME, 'fa-youtube'),
        "youtube.com",
        wait_for_new_window=True
    )

