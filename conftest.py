from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920x1018")
    # chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    username = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")
    username.send_keys("marina@mail.ru")
    password.send_keys("marina123")
    login_button.click()