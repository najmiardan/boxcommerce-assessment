# BoxCommerce Assessment – Selenium Pyton

Automates the sign-up flow on BoxCommerce UAT.

Steps automated:
- Click **“Sign up with email/phone no.”**
- Fill: first name, last name, phone, email, password, confirm password, coupon
- Submit

## Run

```powershell
# Create virtual environment
python -m venv .venv
# Activate virtual environment (Windows)
.venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
# Run tests and generate HTML report
pytest -v --html=report.html --self-contained-html
```

## Configurable via environment vars
- `BOXC_UAT_SIGNUP_URL`
- `BOXC_COUPON`
- `BOXC_TEST_EMAIL` (template with `{suffix}`)
- `BOXC_TEST_PASSWORD`
- `BOXC_FIRST_NAME`, `BOXC_LAST_NAME`, `BOXC_PHONE_NUMBER`
- `HEADLESS`, `IMPLICIT_WAIT`, `EXPLICIT_WAIT`
