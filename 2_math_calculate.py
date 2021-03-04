from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

class test_GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://suninjuly.github.io/get_attribute.html')
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Calculate(self):
        driver = self.driver
        x_element = driver.find_element_by_id('treasure')
        x = x_element.get_attribute("valuex")
     #   x = x_element.text
        y = calc(x)
        input_field = self.driver.find_element_by_id('answer')
        input_field.send_keys(y)

        people_radio = driver.find_element_by_id("peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked == "true", "People radio is not selected by default"

        check_box = self.driver.find_element_by_id('robotCheckbox')
        check_box.click()
        radio_btn = self.driver.find_element_by_id('robotsRule')
        radio_btn.click()
        btnSubmit = self.driver.find_element_by_css_selector('button')
        btnSubmit.click()
        time.sleep(5)
        print(self.driver.find_element_by_id('answer').text)
    

        
if __name__ == '__main__':
   unittest.main()         
