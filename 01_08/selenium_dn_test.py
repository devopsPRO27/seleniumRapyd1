import pytest
from datab import *
from sleniumPOm import *


def test_1(self):
    assert 2 == 2


@pytest.fixture
def driver(self):
    path = '/Users/hothaifa/Desktop/chromedriver'
    driver = webdriver.Chrome(path)
    return driver


@pytest.fixture
def db_connector(self):
    db_connector = DBcon('movieland')
    return db_connector


def test_movie_name(self, driver, db_connector):
    results = db_connector.select('movies', '*')
    actual = results[0][1]

    google_page = GooglePage(driver)
    google_page.search('batman imdb')
    google_page.click_on_link()
    imdb_page = IMDBPage(driver)
    expected = imdb_page.heading_text()

    assert actual == expected
