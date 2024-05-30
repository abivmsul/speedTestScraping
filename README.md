# InternetSpeedTestBot 🚀

## Overview
**SpeedTestBot** is a Python-based automation tool that utilizes Selenium to perform an internet speed test on the Speedtest.net website. It captures the download and upload speeds and displays them in the console.

## Requirements 📦
- Python 3.x
- Selenium
- Google Chrome browser
- ChromeDriver

## Installation 🛠️
### Install Selenium:
```bash
pip install selenium.
```
## How It Works ⚙️💻 
- The script initializes a Chrome browser instance with Selenium.
- It navigates to the Speedtest.net website.
- It waits for the page to fully load and then starts the speed test by clicking the "Go" button.
- After waiting for the test to complete, it captures the download and upload speeds using XPath to locate the respective elements.
- Finally, it prints the results in the console and closes the browser.

## Notes 📝
- The `time.sleep()` calls are used to ensure the page and the speed test have sufficient time to load and complete. Adjust the sleep duration if necessary based on your internet speed and system performance.
- Make sure the ChromeDriver version matches your installed Google Chrome version to avoid compatibility issues.

## Troubleshooting 🛠️
- **Element Not Found**: If the script fails to find elements, ensure that the website structure has not changed and the XPaths are correct.
- **Browser Not Opening**: Ensure that the ChromeDriver executable is in your system's PATH or provide the full path to the `webdriver.Chrome()` initialization.

