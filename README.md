# Playwright Python Login Tests

![Playwright Tests](https://github.com/KalsoomNazar-QA-Engineer/playwright-python-login-tests/actions/workflows/playwright.yml/badge.svg)

Automated UI tests for the login page of [Practice Test Automation](https://practicetestautomation.com/practice-test-login/) using Playwright, Python and pytest, structured with the Page Object Model and integrated with GitHub Actions CI.

## Tools
- Python 3.13
- Playwright
- pytest
- GitHub Actions (CI)

## Project Structure
- `pages/login_page.py`: Page Object Model class (locators and page actions)
- `test_login.py`: test cases (TC_001 to TC_006)
- `requirements.txt`: project dependencies
- `.github/workflows/playwright.yml`: GitHub Actions CI pipeline

## Test Cases Covered
| ID | Scenario | Type |
|---|---|---|
| TC_001 | Valid login with correct credentials | Positive |
| TC_002 | Invalid username with valid password | Negative |
| TC_003 | Valid username with invalid password | Negative |
| TC_004 | Username empty | Negative |
| TC_005 | Password empty | Negative |
| TC_006 | Both fields empty | Negative |

## How to Run
```bash
git clone https://github.com/KalsoomNazar-QA-Engineer/playwright-python-login-tests.git
cd playwright-python-login-tests
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest -v --headed
```

## Result
6 / 6 tests passing locally and in CI (GitHub Actions).

## Author
Kalsoom Nazar, Aspiring QA Engineer