import time
import unittest
from selenium import webdriver #The selenium.webdriver provides all the WebDriver implementations.
from selenium.webdriver.common.keys import Keys #The Keys provide keys in the keyboard like RETURN, F1, ALT etc.

class PythonSeleniumFirstScript(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() # The instance of Firefox WebDriver is created
        self.driver.implicitly_wait (10)  # Wait time in seconds

    # Open
    def test_Events(self):
        driver = self.driver
        driver.get ("http://www.python.org")

        # An assertion to confirm that title has “Submit an Event” word in it
        self.assertIn ("Welcome to Python.org", driver.title)

        # Using Keys class imported from selenium.webdriver.common.keys
        elem = driver.find_element_by_partial_link_text ("Events")
        elem.click ()
        time.sleep (3)

        # An assertion to confirm that title has “Submit an Event” in it
        self.assertIn ("Our Events | Python.org", driver.title)

    # Search in a text box test example
    def test_search(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.minimize_window()

        # An assertion to confirm that title has “Python” word in it
        self.assertIn("Welcome to Python.org", driver.title)

        # Using Keys class imported from selenium.webdriver.common.keys
        elem = driver.find_element_by_name("q")
        elem.send_keys("Java")
        driver.save_screenshot ('C:/Users/Maor/Desktop/Seleniumscreenshot.png')
        elem.send_keys(Keys.RETURN)
        time.sleep (3)

    def test_scroll(self):
            driver = self.driver
            driver.get ( "https://docs.python.org/3" )

            # An assertion to confirm that title has “Python” word in it
            self.assertIn ("3.6.5 Documentation", driver.title )

            # Using Keys class imported from selenium.webdriver.common.keys
            driver.execute_script ("window.scrollTo(0, document.body.scrollHeight);" )
            time.sleep (3)

    # tearDown to quits the driver and close every associated window.
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()