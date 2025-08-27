import os

BASE_URL = os.getenv("BOXC_UAT_SIGNUP_URL", "https://dashboard-uat.boxcommerce.com/en-GB/auth/sign-up")
COUPON_CODE = os.getenv("BOXC_COUPON", "UATQA-DEMO")

TEST_EMAIL = os.getenv("BOXC_TEST_EMAIL", "qa.automation+demo_{suffix}@example.com")
TEST_PASSWORD = os.getenv("BOXC_TEST_PASSWORD", "StrongPassw0rd!")
STORE_FIRST_NAME = os.getenv("BOXC_FIRST_NAME", "QA")
STORE_LAST_NAME = os.getenv("BOXC_LAST_NAME", "Automation")
PHONE_NUMBER = os.getenv("BOXC_PHONE_NUMBER", "81234567890")

HEADLESS = os.getenv("HEADLESS", "true").lower() in {"1","true","yes"}
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "0"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "25"))
