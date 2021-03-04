from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class test_GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.google.com/')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_PageTitle(self):
        self.assertIn('Google', self.driver.title)
        print(self.driver.title)
      
    def test_findInputSearchElementAndEnter(self):
        inputField = self.driver.find_element_by_class_name('gLFyf')
        inputField.send_keys('python')
        inputField.send_keys(Keys.ENTER)

    def test_checkSearchedElements(self):
        driver = self.driver
        inputField = driver.find_element_by_class_name('gLFyf')
        inputField.send_keys('python')
        inputField.send_keys(Keys.ENTER)
        time.sleep(2)

        titles = driver.find_elements_by_xpath('//div[@class="g"]//h3/span')
        for title in titles:
            assert "python" in titles.text.lower()
        
if __name__ == '__main__':
   unittest.main()         
