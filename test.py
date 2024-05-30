import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SpeedTestBot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.up = 0
        self.down = 0

    def getspeed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(15)
        go = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go.click()
        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                       '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print("Down :" + str(self.down))
        print("Up :" + str(self.up))
        self.driver.quit()


Get = SpeedTestBot()
Get.getspeed()
