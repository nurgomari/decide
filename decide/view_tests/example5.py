# Generated by Selenium IDE
import time
import json
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base.tests import BaseTestCase

class TestTestsimpleCreateQuestion(StaticLiveServerTestCase):

    def setUp(self):
        #Load base test functionality for decide
        self.base = BaseTestCase()
        self.base.setUp()

        super_user = User(username='administrator', is_staff=True, is_superuser=True)
        super_user.set_password('administrator')
        super_user.save()

        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-using")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

        super().setUp()            
            
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()
  
    def test_testsimpleCreateQuestion(self):
        self.driver.get(f"{self.live_server_url}/admin/login/?next=/admin/")
        self.driver.set_window_size(1050, 748)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("administrator")
        self.driver.find_element(By.ID, "id_password").send_keys("administrator")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".model-question .addlink").click()
        self.driver.find_element(By.ID, "id_desc").click()
        self.driver.find_element(By.ID, "id_desc").send_keys("ASD")
        self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
        self.driver.find_element(By.ID, "id_options-0-number").click()
        self.driver.find_element(By.ID, "id_options-0-option").click()
        self.driver.find_element(By.ID, "id_options-0-option").send_keys("sss")
        self.driver.find_element(By.ID, "id_options-1-number").send_keys("1")
        self.driver.find_element(By.ID, "id_options-1-number").click()
        self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
        self.driver.find_element(By.ID, "id_options-1-number").click()
        element = self.driver.find_element(By.ID, "id_options-1-number")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "id_options-1-option").click()
        self.driver.find_element(By.ID, "id_options-1-option").send_keys("sss")
        self.driver.find_element(By.NAME, "_save").click()
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4)").click()