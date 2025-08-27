
# BoxCommerce Assessment – Selenium Python

Automates the sign-up flow on BoxCommerce UAT.

## Framework, Tools, and Libraries Used

- **Selenium**: Automates browser actions for end-to-end testing of the signup flow.
- **pytest**: Provides a simple, scalable test runner and fixtures for Python.
- **webdriver-manager**: Automatically downloads and manages browser drivers for Selenium.
- **pytest-html**: Generates detailed HTML reports for test results.

These tools are chosen for their reliability, ease of use, and strong community support for browser automation and reporting in Python.

## How to View Test Results

After running tests, an HTML report is generated (`report.html`).

**Example:**

```powershell
pytest -v --html=report.html --self-contained-html
```

Open `report.html` in your browser to view results. Example image:

![Test Report Example](https://raw.githubusercontent.com/najmiardan/boxcommerce-assessment/main/example-report.png)

## Configurable via Environment Variables

- `BOXC_UAT_SIGNUP_URL`: Target signup page URL
- `BOXC_COUPON`: Coupon code for signup
- `BOXC_TEST_EMAIL`: Email template (use `{suffix}` for randomization)
- `BOXC_TEST_PASSWORD`: Password for signup
- `BOXC_FIRST_NAME`, `BOXC_LAST_NAME`, `BOXC_PHONE_NUMBER`: Default personal info
- `HEADLESS`: Set to `false` to see browser
- `IMPLICIT_WAIT`, `EXPLICIT_WAIT`: Selenium wait times

---

For any issues, please open an issue on GitHub or contact the maintainer.
