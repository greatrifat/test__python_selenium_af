import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "https://alokitofoundation.vercel.app/auth/signin"  # Replace with your login page URL

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver after all tests
        cls.driver.quit()

    def test_valid_login(self):
        """Test valid login credentials."""
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "email").send_keys("greatrifat@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("1234")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
        
        
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"1.Valid Alert text: {alert_text}")
            self.assertEqual(alert_text, "Signin successful", f"Unexpected alert text: {alert_text}")
            alert.accept()
        except Exception as e:
            self.fail(f"Alert did not appear: {e}")

    def test_invalid_email(self):
        """Test login with invalid email."""
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "email").send_keys("invalid@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("1234")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"2.Invalid Alert text: {alert_text}")
            self.assertEqual(alert_text, "User not found", f"Unexpected alert text: {alert_text}")
            alert.accept()
        except Exception as e:
            self.fail(f"Alert did not appear: {e}")

    def test_invalid_password(self):
        """Test login with valid email but invalid password."""
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "email").send_keys("greatrifat@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"3.invalid pass Alert text: {alert_text}")
            self.assertEqual(alert_text, "Wrong Password", f"Unexpected alert text: {alert_text}")
            alert.accept()
        except Exception as e:
            self.fail(f"Alert did not appear: {e}")

    def test_empty_email(self):
        """Test login with empty email field."""
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "email").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("1234")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"4.empty email Alert text: {alert_text}")
            self.assertEqual(alert_text, "Please provide both email and password", f"Unexpected alert text: {alert_text}")
            alert.accept()
        except Exception as e:
            self.fail(f"Alert did not appear: {e}")

    def test_empty_password(self):
        """Test login with empty password field."""
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "email").send_keys("greatrifat@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"5.empty pass Alert text: {alert_text}")
            self.assertEqual(alert_text, "Please provide both email and password", f"Unexpected alert text: {alert_text}")
            alert.accept()
        except Exception as e:
            self.fail(f"Alert did not appear: {e}")

    def test_empty_credentials(self):
        """Test login with both fields empty."""
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "email").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"6.both empth Alert text: {alert_text}")
            self.assertEqual(alert_text, "Please provide both email and password", f"Unexpected alert text: {alert_text}")
            alert.accept()
        except Exception as e:
            self.fail(f"Alert did not appear: {e}")


if __name__ == "__main__":
    with open("test_report.txt", "w") as report_file:
        runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
        unittest.main(testRunner=runner, exit=False)



