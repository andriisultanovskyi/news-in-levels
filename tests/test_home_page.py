import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


def open_homepage(browser):
    browser.get("https://www.newsinlevels.com/")
    time.sleep(2)


# The test checks the click of the "Level 1" button on the header and goes to the first level news page
def test_click_button_level_1_header(browser):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Level 1'][1]"))
    )
    element.click()
    WebDriverWait(browser, 10).until(EC.url_contains("level/level-1"))
    assert "https://www.newsinlevels.com/level/level-1/" in browser.current_url


# The test checks the click of the "Level 2" button on the header and goes to the first level news page
def test_click_button_level_2_header(browser):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Level 2'][1]"))
    )
    element.click()
    WebDriverWait(browser, 10).until(EC.url_contains("level/level-2"))
    assert "https://www.newsinlevels.com/level/level-2/" in browser.current_url


# The test checks the click of the "Level 3" button on the header and goes to the first level news page
def test_click_button_level_3_header(browser):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Level 3'][1]"))
    )
    element.click()
    WebDriverWait(browser, 10).until(EC.url_contains("level/level-3"))
    assert "https://www.newsinlevels.com/level/level-3/" in browser.current_url


# The test checks the click of the "Days" button on the header and goes to the 'Days in Levels' page
def test_click_button_days(browser, switch_to_new_window_home):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'DAYS'))
    )
    element.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("daysinlevels.com"))
    assert "https://www.daysinlevels.com/?utm_source=NiLMenu" in browser.current_url


# The test checks the click of the "Book 1" button on the header and goes to the 'Robinson Crusoe in Levels' page
def test_click_button_book_1(browser, switch_to_new_window_home):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'BOOK 1'))
    )
    element.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("robinsoncrusoeinlevels.com"))
    assert "https://www.robinsoncrusoeinlevels.com/?utm_source=NiLMenu" in browser.current_url


# The test checks the click of the "Grammar" button on the header and goes to the 'Grammar in Levels' page
def test_click_button_grammar(browser, switch_to_new_window_home):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='GRAMMAR']"))
    )
    element.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("grammarinlevels.com"))
    assert "https://www.grammarinlevels.com/?utm_source=NiLMenu" in browser.current_url


# The test checks the click of the "Book 2" button on the header and goes to the 'The Little Prince in Levels' page
def test_click_button_book_2(browser, switch_to_new_window_home):
    open_homepage(browser)
    print('browser opened')
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'BOOK 2'))
    )
    print("Before click:", browser.window_handles)
    element.click()
    time.sleep(2)
    print("After click:", browser.window_handles)
    switch_to_new_window_home()
    print('new window opened')
    WebDriverWait(browser, 10).until(EC.url_contains("thelittleprinceinlevels.com"))
    assert "https://www.thelittleprinceinlevels.com/?utm_source=NiLMenu" in browser.current_url


# The test checks the click of the "Learn" button on the header and goes to the 'How to Learn English' page
def test_click_button_learn(browser, switch_to_new_window_home):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'LEARN'))
    )
    element.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("howtolearnenglishinlevels.com"))
    assert "https://www.howtolearnenglishinlevels.com/?utm_source=NiLMenu" in browser.current_url


# The test checks the click of the "Video" button on the header and goes to the 'Videos in Levels' page
def test_click_button_video(browser, switch_to_new_window_home):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='VIDEO']"))
    )
    element.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("videosinlevels.com"))
    assert "https://www.videosinlevels.com./?utm_source=NiLMenu" in browser.current_url


# The test checks the click of the "Skype" button on the header and goes to the 'Speak in Levels' page
def test_click_button_skype(browser, switch_to_new_window_home):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='SKYPE']"))
    )
    element.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("speakinlevels.com"))
    assert "https://www.speakinlevels.com/?utm_source=NiLMenu" in browser.current_url


# The test checks the click of the "Test" button on the header and goes to the 'Test for Students' page
def test_click_button_test(browser, switch_to_new_window_home):
    open_homepage(browser)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='TEST']"))
    )
    element.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("testlanguages.com"))
    assert "https://www.testlanguages.com/?utm_source=NiLMenu" in browser.current_url


def click_level_button_and_check_redirect(browser, time_str, level):
    now = datetime.now()
    if now.hour < int(time_str.split(":")[0]):
        pytest.skip(f"Before {time_str} - test skipped")
    date_str = now.strftime("%d-%m-%Y")
    full_text = f"{date_str} {time_str}"
    browser.get("https://www.newsinlevels.com/")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'news-block')))
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, f"//p[text()='{full_text}']")))
    except:
        pytest.skip(f"Element with date and time '{full_text}' not found")
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH,
            f"//div[contains(@class, 'news-block-right') and .//p[text()='{full_text}']]//a[text()='Level {level}']"))
    )
    button.click()
    wait.until(lambda driver: "https://www.newsinlevels.com/products/" in driver.current_url)
    assert "https://www.newsinlevels.com/products/" in browser.current_url and f"level-{level}" in browser.current_url, \
        f"Unexpected URL: {browser.current_url}"


@pytest.mark.skipif(datetime.today().weekday() >= 5, reason="Day off (Sat/Sun)")


@pytest.mark.parametrize("time_str,level", [
    ("07:00", 1),
    ("07:00", 2),
    ("07:00", 3),
    ("15:00", 1),
    ("15:00", 2),
    ("15:00", 3),
])
def test_click_level_button(browser, time_str, level):
    click_level_button_and_check_redirect(browser, time_str, level)


# The test checks the click of the "Test Languages" link and goes to the 'Test for Students' page
def test_click_link_test_languages(browser, switch_to_new_window_home):
    open_homepage(browser)
    click_link_test_languages = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Test Languages']"))
    )
    click_link_test_languages.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("testlanguages.com"))
    assert "https://www.testlanguages.com/?utm_source=manual" in browser.current_url


# The test checks the click of the "Skype Section" link and goes to the 'Speak in English' page
def test_click_link_skype_section(browser, switch_to_new_window_home):
    open_homepage(browser)
    click_link_skype_section = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Skype section'))
    )
    click_link_skype_section.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("speakinlevels.com"))
    assert "https://www.speakinlevels.com/" in browser.current_url


# The test checks the click of the "Speak in Levels" link and goes to the 'Speak in Levels' page
def test_click_link_speak_in_levels(browser, switch_to_new_window_home):
    open_homepage(browser)
    click_link_speak_in_levels = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Speak in Levels'))
    )
    click_link_speak_in_levels.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("speakinlevels.com"))
    assert "https://www.speakinlevels.com/what-to-talk-about/" in browser.current_url


# The test checks the click of the "Depositphotos" link and goes to the 'depositphotos' page
def test_click_link_depositphotos(browser, switch_to_new_window_home):
    open_homepage(browser)
    click_link_depositphotos = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Depositphotos'))
    )
    click_link_depositphotos.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("depositphotos.com"))
    assert "https://depositphotos.com/" in browser.current_url


# The test checks the click of the "Facebook" icon and goes to the 'Facebook News in Levels' page
def test_click_icon_facebook(browser, switch_to_new_window_home):
    open_homepage(browser)
    click_icon_facebook = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'facebook'))
    )
    click_icon_facebook.click()
    switch_to_new_window_home()
    WebDriverWait(browser, 10).until(EC.url_contains("facebook.com"))
    assert "https://www.facebook.com/newsinlevels/" in browser.current_url


# The test checks the click of the "About Us" link and goes to the 'About Us' page
def test_click_link_about_us(browser):
    open_homepage(browser)
    click_link_about_us = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'About Us'))
    )
    click_link_about_us.click()
    WebDriverWait(browser, 10).until(EC.url_contains("newsinlevels.com/about-us/"))
    assert "https://www.newsinlevels.com/about-us/" in browser.current_url


# The test checks the click of the "Contact" link and goes to the 'Contact' page
def test_click_link_contact(browser):
    open_homepage(browser)
    click_link_contact = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Contact'))
    )
    click_link_contact.click()
    WebDriverWait(browser, 10).until(EC.url_contains("newsinlevels.com/contact/"))
    assert "https://www.newsinlevels.com/contact/" in browser.current_url


# The test checks the click of the "Conditions of Use" link and goes to the 'Conditions of Use' page '
def test_click_link_conditions_of_use(browser):
    open_homepage(browser)
    click_link_conditions_of_use = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Conditions of Use'))
    )
    click_link_conditions_of_use.click()
    WebDriverWait(browser, 10).until(EC.url_contains("newsinlevels.com/conditions-of-use/"))
    assert "https://www.newsinlevels.com/conditions-of-use/" in browser.current_url


