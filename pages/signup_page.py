from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver, base_url, timeout=30):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    EMAIL_SIGNUP_BUTTON = (By.XPATH, "//button[.//span[contains(., 'Sign up with email')]]")
    FIRST_NAME = (By.CSS_SELECTOR, "input[placeholder='First name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='Last name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone number']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'], input[placeholder='Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
    CONFIRM_INPUT = (By.CSS_SELECTOR, "input[placeholder='Confirm password']")
    COUPON_INPUT = (By.CSS_SELECTOR, "input[placeholder='Coupon code']")
    SIGNUP_BUTTON = (By.XPATH, "//button[normalize-space()='SIGN UP' or @type='submit']")
    SUCCESS_URL_HINTS = ("/onboarding", "/dashboard")

    def open(self):
        self.driver.get(self.base_url)
        return self

    def start_email_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_SIGNUP_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
        return self

    def fill_name(self, first_name, last_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        return self

    def fill_phone(self, phone_number):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone_number)
        return self

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        return self

    def fill_passwords(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.CONFIRM_INPUT).send_keys(password)
        return self

    def fill_coupon(self, coupon):
        self.driver.find_element(*self.COUPON_INPUT).send_keys(coupon)
        return self

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BUTTON)).click()
        return self

    def wait_for_success(self, timeout=45):
        WebDriverWait(self.driver, timeout).until(
            lambda d: any(hint in d.current_url for hint in self.SUCCESS_URL_HINTS)
        )
