import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Test: Checking the presence of an input field and a search button
def test_search_elements_exist(browser):
    search_input = browser.find_element(By.ID, "s")
    search_button = browser.find_element(By.ID, "searchsubmit")
    assert search_input.is_displayed()
    assert search_button.is_displayed()


# Test: Performing a search and checking the results
@pytest.mark.parametrize("query", ["test", "Berlin", "pytest"], ids=["search_test", "search_berlin", "search_pytest"])
def test_search_functionality(browser, query):
    search_input = browser.find_element(By.NAME, "s")
    search_button = browser.find_element(By.ID, "searchsubmit")
    search_input.clear()
    search_input.send_keys(query)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "searchsubmit")))
    search_button.click()
    WebDriverWait(browser, 10).until(lambda driver: query in driver.current_url) # Waiting for URL change
    expected_url = f"https://www.newsinlevels.com/?s={query}" # Form the expected URL
    assert browser.current_url == expected_url, f"Expected {expected_url}, Received {browser.current_url}"


# Test: Checking the search operation when entering via ENTER
def test_search_via_enter(browser):
    search_input = browser.find_element(By.NAME, "s")
    search_input.clear()
    search_input.send_keys("Schwarzenegger")
    search_input.send_keys(Keys.RETURN)  # Simulate pressing Enter
    browser.implicitly_wait(5)
    browser.find_elements(By.NAME, 'Search Result For')
    assert "https://www.newsinlevels.com/?s=Schwarzenegger" in browser.current_url


# Test: Search by empty query
def test_search_empty_query(browser):
    search_input = browser.find_element(By.NAME, "s")
    search_button = browser.find_element(By.ID, "searchsubmit")
    search_input.clear()
    search_button.click()
    browser.implicitly_wait(5)
    browser.find_elements(By.NAME, 'Search Result For')
    assert "https://www.newsinlevels.com/?s=" in browser.current_url


# Test: Checking the presence of an input field and a search button
def test_search_elements_exist_days(driver):
    search_input = driver.find_element(By.ID, "s")
    search_button = driver.find_element(By.ID, "searchsubmit")
    assert search_input.is_displayed()
    assert search_button.is_displayed()

# Test: Performing a search and checking the results
@pytest.mark.parametrize("query", ["pirates", "photograph", "pytest"], ids=["search_pirates", "search_photograph", "search_pytest"])
def test_search_functionality_days(driver, query):
    search_input = driver.find_element(By.ID, "s")
    search_button = driver.find_element(By.ID, "searchsubmit")
    search_input.clear()
    search_input.send_keys(query)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "searchsubmit")))
    search_button.click()
    WebDriverWait(driver, 10).until(lambda driver: query in driver.current_url) # Waiting for URL change
    expected_url = f"https://www.daysinlevels.com/?s={query}" # Form the expected URL
    assert driver.current_url == expected_url, f"Expected {expected_url}, Received {driver.current_url}"


# Test: Checking the search operation when entering via ENTER
def test_search_via_enter_days(driver):
    search_input = driver.find_element(By.NAME, "s")
    search_input.clear()
    search_input.send_keys("Leonardo")
    search_input.send_keys(Keys.RETURN)  # Simulate pressing Enter
    driver.implicitly_wait(5)
    driver.find_elements(By.NAME, 'Search Result For')
    assert "https://www.daysinlevels.com/?s=Leonardo" in driver.current_url


# Test: Search by empty query
def test_search_empty_query_days(driver):
    search_input = driver.find_element(By.NAME, "s")
    search_button = driver.find_element(By.ID, "searchsubmit")
    search_input.clear()
    search_button.click()
    driver.implicitly_wait(5)
    driver.find_elements(By.NAME, 'Search Result For')
    assert "https://www.daysinlevels.com/?s=" in driver.current_url
