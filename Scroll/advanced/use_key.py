import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

ss_path = "/Applications/PHP/"


class TestCreateAppPHP(EnvironmentSetup):

    def test_Laravel_default_01(self):
        # pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver

        driver.get("https://www.w3schools.com/")
        time.sleep(5)

        elem = driver.find_element(By.XPATH, "//body/div[@id='main']/div[3]/div[1]/div[1]/a[3]")
        elem.send_keys(Keys.PAGE_DOWN)
        # actions.perform()
        time.sleep(5)

        # actions.moveToElement(element);
        # ## actions.click();
        # actions.perform();