import time, uuid, random, string
import pytest
from utils import config
from pages.signup_page import SignupPage

@pytest.mark.signup
def test_signup_with_coupon(driver):
    suffix = str(int(time.time())) + "-" + uuid.uuid4().hex[:6]
    email = config.TEST_EMAIL.format(suffix=suffix)

    first_name = "QA" + ''.join(random.choices(string.ascii_uppercase, k=4))
    last_name = "Automation" + ''.join(random.choices(string.ascii_uppercase, k=4))

    phone_number = "8" + ''.join(random.choices(string.digits, k=10))

    page = SignupPage(driver, config.BASE_URL, timeout=config.EXPLICIT_WAIT)
    page.open().start_email_signup()
    page.fill_name(first_name, last_name)\
        .fill_phone(phone_number)\
        .fill_email(email)\
        .fill_passwords(config.TEST_PASSWORD)\
        .fill_coupon(config.COUPON_CODE)\
        .submit()

    page.wait_for_success(timeout=max(30, config.EXPLICIT_WAIT))
    assert any(hint in driver.current_url for hint in ["/onboarding", "/dashboard"]), f"Signup failed, current URL: {driver.current_url}"
