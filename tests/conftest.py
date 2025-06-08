import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile
import shutil
import logging
import os
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, ElementNotInteractableException


# Logging settings
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-default-browser-check")
    # options.add_argument("--no-first-run")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--user-data-dir=/tmp/selenium-user-data")
    # options.add_argument("--headless")
    # options.add_argument("--headless=new")
    options.add_argument("--headless=old")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture()
def switch_to_new_window_home(browser):
    """Waits for a new window to open and switches to it"""
    def _switch():
        WebDriverWait(browser, 5).until(lambda d: len(d.window_handles) > 1)
        windows = browser.window_handles
        print(f"Open windows: {windows}")
        if len(windows) > 1:
            browser.switch_to.window(windows[1])
        else:
            pytest.fail("New window did not open")
    return _switch


@pytest.fixture()
def browser():
    browser = create_driver()
    browser.get('https://www.newsinlevels.com/')
    time.sleep(2)
    browser.maximize_window()
    try:
        close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'fc-icon-button'))
        )
        close_button.click()
    except TimeoutException:
        print("The dialog box did not appear, we continue the test")
    yield browser
    browser.quit()


@pytest.fixture()
def driver():
    driver = create_driver()
    driver.get('https://www.daysinlevels.com/?utm_source=NiLMenu')
    driver.maximize_window()
    try:
        # Wait for the modal window title to appear
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "fc-dialog-headline"))
        )
        # Find and click on the close icon (cross)
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-cancel-icon-svg"))
        )
        close_button.click()
        print("The modal window has been closed")
    except TimeoutException:
        print("The dialog box did not appear, we continue the test")
    time.sleep(2)
    yield driver
    # Remove the interfering image manually
    driver.execute_script("""
            const popupImg = document.querySelector('img.aligncenter[src*="Test-popup.jpg"]');
            if (popupImg) {
                popupImg.remove();
                console.log("🧹 Popup image removed");
            }
        """)
    time.sleep(1)
    driver.quit()


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


@pytest.fixture()
def book_1():
    book_1 = create_driver()
    book_1.get('https://www.robinsoncrusoeinlevels.com/?utm_source=NiLMenu')
    time.sleep(2)
    book_1.maximize_window()
    try:
        close_button = WebDriverWait(book_1, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'fc-icon-button'))
        )
        close_button.click()
    except TimeoutException:
        print("The dialog box did not appear, we continue the test")
    yield book_1
    book_1.quit()


@pytest.fixture()
def grammar():
    grammar = create_driver()
    grammar.get('https://www.grammarinlevels.com/?utm_source=NiLMenu')
    time.sleep(2)
    grammar.maximize_window()
    try:
        close_button = WebDriverWait(grammar, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'fc-icon-button'))
        )
        close_button.click()
    except TimeoutException:
        print("The dialog box did not appear, we continue the test")
    yield grammar
    grammar.quit()


@pytest.fixture()
def switch_to_new_window(grammar):
    """Waits for a new window to open and switches to it"""
    def _switch():
        WebDriverWait(grammar, 5).until(lambda d: len(d.window_handles) > 1)
        windows = grammar.window_handles
        print(f"Open windows: {windows}")
        if len(windows) > 1:
            grammar.switch_to.window(windows[1])
        else:
            pytest.fail("New window did not open")
    return _switch


@pytest.fixture()
def book_2():
    book_2 = create_driver()
    book_2.get('https://www.thelittleprinceinlevels.com/?utm_source=NiLMenu')
    time.sleep(2)
    book_2.maximize_window()
    try:
        close_button = WebDriverWait(book_2, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'fc-icon-button'))
        )
        close_button.click()
    except TimeoutException:
        print("The dialog box did not appear, we continue the test")
    yield book_2
    book_2.quit()


@pytest.fixture()
def learn():
    learn = create_driver()
    learn.get('https://www.howtolearnenglishinlevels.com/?utm_source=NiLMenu')
    time.sleep(2)
    learn.maximize_window()
    try:
        close_button = WebDriverWait(learn, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'fc-icon-button'))
        )
        close_button.click()
    except TimeoutException:
        print("The dialog box did not appear, we continue the test")
    yield learn
    learn.quit()


@pytest.fixture()
def video():
    video = create_driver()
    video.get('https://www.videosinlevels.com/?utm_source=NiLMenu')
    time.sleep(2)
    video.maximize_window()
    try:
        close_button = WebDriverWait(video, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'fc-icon-button'))
        )
        close_button.click()
    except TimeoutException:
        print("The dialog box did not appear, we continue the test")
    yield video
    video.quit()


# Test fall hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Automatic screenshot when test fails.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = None
        for fixture_name, fixture_value in item.funcargs.items():
            if hasattr(fixture_value, "save_screenshot"):
                driver = fixture_value
                break

        if driver:
            if not os.path.exists("../screenshots"):
                os.makedirs("../screenshots")

            screenshot_path = os.path.join("../screenshots", f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            logger.info(f"[!] Screenshot saved: {screenshot_path}")
        else:
            logger.warning("[!] Screenshot NOT saved: Driver not found in fixtures.")


def click_and_wait_url(driver, xpath, expected_url_part, expected_full_url, scroll=False):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    if scroll:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
    element.click()
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url_part))
    assert expected_full_url in driver.current_url