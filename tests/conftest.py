import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils import config

@pytest.fixture(scope="session")
def driver():
    options = ChromeOptions()
    if config.HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    if config.IMPLICIT_WAIT:
        drv.implicitly_wait(config.IMPLICIT_WAIT)
    yield drv
    drv.quit()
