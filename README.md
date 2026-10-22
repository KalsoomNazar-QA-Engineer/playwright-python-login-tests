# Playwright Python Login Tests

Automated UI tests for the login page of [Practice Test Automation](https://practicetestautomation.com/practice-test-login/) using Playwright, Python and pytest.

## Tools
- Python 3.13
- Playwright
- pytest

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
pip install pytest-playwright
playwright install chromium
pytest --headed
```

## Result
6 / 6 tests passing.

## Author
Kalsoom Nazar, Aspiring QA Engineer