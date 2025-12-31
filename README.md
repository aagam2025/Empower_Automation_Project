# Playwright Pytest Automation Framework

A scalable and maintainable end-to-end web automation testing framework built using Python, Playwright, and Pytest.

This framework follows best practices such as the Page Object Model (POM) and a clean test structure to support reliable and efficient automated testing.

🚀 **Tech Stack**:
- Python 3.14.2
- Playwright (Python)
- Pytest

📂 **Project Structure**:
```
PLAYWRIGHT/
│
├── config/
│ └── config.py # Application configuration (URLs, credentials, etc.)
│
├── pages/ # Page Object Model (POM) classes
│ ├── base_page.py # Common page-level actions
│ ├── login_page.py
│ ├── signup_page.py
│ ├── dashboard_page.py
│ ├── courses_page.py
│ ├── library_page.py
│ ├── policies_page.py
│ └── surveys_page.py
│
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_signup.py
│ ├── test_dashboard.py
│ ├── test_add_courses.py
│ ├── test_library.py
│ ├── test_policies.py
│ └── test_surveys.py
│
├── conftest.py # Pytest fixtures (browser & page setup)
├── pytest.ini # Pytest configuration
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```


✅ Features:
1. End-to-end web automation using Playwright
2. Pytest-based test execution
3. Page Object Model (POM) design pattern
4. Clean and reusable test logic
5. Supports modern web applications
6. Easy to extend and maintain

🔧 Installation & Setup:

1. Clone the Repository:
```
git clone <repository-url>
cd <project-folder>
```
2. Create Virtual Environment (Optional but Recommended):
```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
3. Install Dependencies:
```
pip install -r requirements.txt
```
4. Install Playwright Browsers:
```
playwright install
```

## ⚙️ Pytest Configuration (pytest.ini):
This project uses a pytest.ini file to define default Pytest behavior, so common options do not need to be passed from the command line every time.
Typical configuration includes:
- -v for verbose test output
- -s to allow print statements and logs in the console
- Test discovery paths

This keeps test execution clean and consistent across environments.

▶️ Running Tests:

Pytest options like -v and -s are already configured in pytest.ini, so you do not need to pass them explicitly while running tests.

1. Run all tests:
```
pytest
```
2. Run tests in headed mode (if configured via fixtures):
```
pytest --headed
```
3. Run a specific test file:
```
pytest tests/test_login.py
```
4. Run tests with verbose output:
```
pytest -v
```

🧪 Writing Tests
- Tests are written using Pytest
- Page-specific actions and locators are maintained inside the pages/ folder
- Tests should only contain assertions and test flow logic

Example:
```
def test_login(page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.login()
```

📌 Best Practices Followed:
- Page Object Model (POM)
- Separation of test logic and UI interactions
- Minimal hard waits (uses Playwright auto-waiting)
- Readable and maintainable code structure

📈 Future Enhancements:
- Add reporting (Allure / HTML reports)
- Environment-based configuration
- CI/CD integration (GitHub Actions)
- Cross-browser execution

👨‍💻 Author:

Aagam Desai

Automation Engineer | Python | Playwright | Pytest

📄 License:

This project is for learning and automation practice purposes.
