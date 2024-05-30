from selenium import webdriver


class SpeedTestBot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.up = 0
        self.down = 0


Get = SpeedTestBot()
