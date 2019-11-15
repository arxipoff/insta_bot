import selenium
from selenium import webdriver
import time

# скачиваем драйвер для конкретной версии браузера, указываем путь! писалось на версии Версия 78.0.3904.97 (Официальная сборка), (64 бит)
browser = webdriver.Chrome("/Users/v.arhipov/Desktop/python/insta_bot/chromedriver")

# указываем какую страницу открыть
browser.get("https://www.instagram.com/")
# ждем
time.sleep(1)
# входим в аккаунт
browser.get("https://www.instagram.com/accounts/login")
# ждем
time.sleep(1)
# вводим логин пароль
browser.find_element("name", "username").send_keys("")
browser.find_element("name", "password").send_keys("")
browser.find_element("xpath", "//section/main/div/article/div/div[1]/div/form/div[4]/button").click()
# ждем
time.sleep(3)

# продолжение следует ...