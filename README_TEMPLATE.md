# DailyCal Mobile App Automation Framework

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Appium](https://img.shields.io/badge/Appium-2.0-green.svg)](http://appium.io/)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-orange.svg)](https://pytest.org/)

A comprehensive mobile automation framework for testing the DailyCal Android application using Appium, Selenium, and Pytest.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Test Coverage](#test-coverage)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This automation framework provides comprehensive test coverage for the DailyCal mobile application, including:
- Complete sign-in flow (6 steps)
- Exercise logging (Run, Weight Lifting, Manual, AI-powered)
- Food management (Scan, Save, Database)
- Nutrition tracking
- Water intake management
- Weight management
- Today's burn calculations

**Total Test Coverage:** ~155-220 test cases

## ✨ Features

- ✅ Page Object Model (POM) design pattern
- ✅ Data-driven testing with JSON test data
- ✅ Cross-platform compatibility (Windows, Linux, macOS)
- ✅ Comprehensive error handling and retry mechanisms
- ✅ Detailed test reporting
- ✅ Modular and maintainable code structure

## 📦 Prerequisites

Before running the tests, ensure you have the following installed:

### Required Software

1. **Python 3.9 or higher**
   ```bash
   python --version
   ```

2. **Appium Server**
   ```bash
   npm install -g appium
   appium --version
   ```

3. **Android SDK**
   - Android Studio or standalone SDK
   - ADB (Android Debug Bridge)
   - Set ANDROID_HOME environment variable

4. **Java JDK 8 or higher**
   ```bash
   java -version
   ```

5. **Node.js and npm** (for Appium)
   ```bash
   node --version
   npm --version
   ```

### Required Hardware

- Android device (physical or emulator)
- USB cable (for physical device)
- Stable internet connection

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/DailyCal_Automation.git
cd DailyCal_Automation
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Appium Drivers

```bash
appium driver install uiautomator2
```

### Step 5: Start Appium Server

```bash
# In a separate terminal
appium
```

## ⚙️ Configuration

### Environment Setup

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file with your configuration:
   ```env
   # Appium Configuration
   APPIUM_SERVER_URL=http://127.0.0.1:4723/wd/hub
   
   # App Configuration
   APP_PACKAGE=com.dailycalai.app
   APP_ACTIVITY=com.dailycalai.app.MainActivity
   APK_PATH=path/to/your/app.apk
   
   # Device Configuration
   DEVICE_UDID=  # Leave empty for auto-detection
   USE_EMULATOR=false
   
   # Timeouts
   DEFAULT_TIMEOUT=30
   ```

### Device Setup

#### Physical Device:
1. Enable Developer Options on your Android device
2. Enable USB Debugging
3. Connect device via USB
4. Verify connection:
   ```bash
   adb devices
   ```

#### Emulator:
1. Start Android emulator from Android Studio
2. Verify connection:
   ```bash
   adb devices
   ```

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests by Marker

```bash
# Run sign-in tests only
pytest -m signin

# Run core feature tests
pytest -m run_feature

# Run regression tests
pytest -m regression
```

### Run Specific Test File

```bash
pytest tests/test_signin_functionality.py
```

### Run with HTML Report

```bash
pytest --html=reports/test_report.html --self-contained-html
```

### Run with Verbose Output

```bash
pytest -v
```

### Run Specific Test Case

```bash
pytest tests/test_signin_functionality.py::test_step1 -v
```

## 📁 Project Structure

```
DailyCal_Automation/
│
├── core/                          # Core utilities and configurations
│   ├── __init__.py
│   ├── driver_setup.py           # Appium driver initialization
│   ├── activities.py             # Common actions (click, fill, etc.)
│   ├── locators.py               # Page Object locators
│   └── necessary_packages.py     # Shared imports
│
├── features/                      # Feature-specific page objects
│   ├── home_page.py
│   ├── nutrition_page.py
│   ├── water_settings_page.py
│   ├── update_current_weight_page.py
│   └── update_goal_weight_page.py
│
├── signin_pages/                  # Sign-in flow pages
│   ├── Step1.py
│   ├── Step2.py
│   ├── Step3.py
│   ├── Step4.py
│   ├── Step5.py
│   └── Step6.py
│
├── core_features_regression/      # Core feature implementations
│   ├── exercise.py
│   ├── scan_food.py
│   └── save_food.py
│
├── premium_features/              # Premium feature implementations
│   ├── exercise/
│   ├── food_database/
│   └── scan_food/
│
├── tests/                         # Test files
│   ├── conftest.py               # Pytest fixtures
│   ├── test_signin_functionality.py
│   ├── test_core_feature_functionality.py
│   └── ...
│
├── Test Data/                     # JSON test data files
│   ├── Signin_pages/
│   ├── Features/
│   ├── Water_settings/
│   └── ...
│
├── reports/                       # Test reports
│   └── assets/
│
├── config/                        # Configuration files
│   ├── config.py
│   └── .env.example
│
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest configuration
├── .env.example                   # Environment variables template
└── README.md                      # This file
```

## 📊 Test Coverage

### Feature Coverage

| Feature Area | Test Cases | Coverage % |
|--------------|------------|------------|
| Sign-In Flow | 50-60 | 90% |
| Exercise Features | 30-40 | 85% |
| Food Features | 20-25 | 80% |
| Nutrition Page | 25-30 | 85% |
| Water Settings | 15-20 | 90% |
| Weight Management | 15-20 | 85% |
| Today's Burn | 20-30 | 80% |
| Integration Tests | 5-10 | 70% |
| **TOTAL** | **155-220** | **~85%** |

## 🐛 Troubleshooting

### Common Issues

#### Issue: "No connected Android devices found"
**Solution:**
- Check if device is connected: `adb devices`
- Enable USB Debugging on device
- Install USB drivers if needed

#### Issue: "Appium server not running"
**Solution:**
- Start Appium server: `appium`
- Check if port 4723 is available
- Verify Appium installation: `appium --version`

#### Issue: "Module not found" errors
**Solution:**
- Activate virtual environment
- Install dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version`

#### Issue: "Element not found" errors
**Solution:**
- Increase timeout in config
- Check if app is installed on device
- Verify locators in `core/locators.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Run tests: `pytest`
5. Commit changes: `git commit -m "Add new feature"`
6. Push to branch: `git push origin feature/new-feature`
7. Create Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to all functions
- Write unit tests for new features
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Appium community
- Selenium community
- Pytest framework

## 📞 Support

For issues and questions:
- Create an issue in GitHub
- Contact: your.email@company.com

---

**Last Updated:** 2024  
**Version:** 1.0.0

