from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.instagram.com/accounts/login/")
print("👉 Inicia sesión en Instagram (usuario, contraseña y 2FA si aplica).")
input("Presiona ENTER cuando hayas terminado el login...")

cookies = driver.get_cookies()
with open("cookies_instagram.json", "w") as f:
    json.dump(cookies, f)

print("✅ Cookies de Instagram guardadas en cookies_instagram.json")
driver.quit()
