import pytest
from conftest import click_and_wait_url


# The test checks the click of the "Home" link and goes to the 'Videos in levels' page
def test_click_link_home(video):
    print(video.current_url)
    print(video.page_source)
    click_and_wait_url(
        video,
        '//a[@href="/" and text()="Home"]',
        "videosinlevels.com",
        "https://www.videosinlevels.com/"
    )


# The test checks the click of the "Level 1, 2, 3, 4, 5, 6" link and goes to the 'Videos in levels Level 1, 2, 3, 4, 5, 6' page
@pytest.mark.parametrize("level, url_part", [
    (1, "/level-1/"),
    (2, "/level-2/"),
    (3, "/level-3/"),
    (4, "/level-4/"),
    (5, "/level-5/"),
    (6, "/level-6/"),
])
def test_click_link_levels(video, level, url_part):
    xpath = f"//a[text()='Level {level}']"
    expected_url = f"https://www.videosinlevels.com/category/level-{level}/"
    print(video.current_url)
    print(video.page_source)
    click_and_wait_url(video, xpath, url_part, expected_url)


# The test checks the click of the "Older posts" button and goes to the 'Page 2'
def test_click_button_older_posts(video):
    video.get("https://www.videosinlevels.com/")
    print(video.current_url)
    print(video.page_source)
    click_and_wait_url(
        video,
        "//a[contains(@href, '/page/2')]",
        "/page/2/",
        "https://www.videosinlevels.com/page/2/",
        scroll=True
    )

