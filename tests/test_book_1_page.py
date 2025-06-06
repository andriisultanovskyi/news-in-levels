import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_and_assert(driver, locator, expected_url_part, expected_full_url, by=By.XPATH):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, locator))
    )
    element.click()
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url_part))
    assert expected_full_url in driver.current_url

# The tests check the click of the "level 1, 2, 3" Links and go to the 'Robinson Crusoe level 1, 2, 3' pages
@pytest.mark.parametrize("link_text, expected_url", [
    ("Level 1", "https://www.robinsoncrusoeinlevels.com/level1/"),
    ("Level 2", "https://www.robinsoncrusoeinlevels.com/level2/"),
    ("Level 3", "https://www.robinsoncrusoeinlevels.com/level3/"),
])
def test_click_level_links(book_1, link_text, expected_url):
    locator = f"//*[text()='{link_text}'][1]"
    click_and_assert(
        book_1,
        locator=locator,
        expected_url_part=expected_url.split("/")[-2],
        expected_full_url=expected_url
    )


# The test checks the click of the "three levels" Link and goes to the 'how to use' page
def test_click_link_three_levels(book_1):
    click_and_assert(
        book_1,
        locator="//*[text()='three levels']",
        expected_url_part="robinsoncrusoeinlevels.com/how-to-use/",
        expected_full_url="https://www.robinsoncrusoeinlevels.com/how-to-use/"
    )


# The test checks the click of the "Next chapter" button and goes to the 'Next chapter' page
def test_click_button_next_chapter(book_1):
    click_and_assert(
        book_1,
        locator="//*[text()='Next chapter']",
        expected_url_part="robinsoncrusoeinlevels.com/level1/chapter2/",
        expected_full_url="https://www.robinsoncrusoeinlevels.com/level1/chapter2/"
    )
