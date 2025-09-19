import os, sys, time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def load_cookies(driver, cookie_file):
    driver.get("https://www.instagram.com/")
    with open(cookie_file, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(5)


def post_image(image_path, caption, cookie_file="/root/proyectos/social_auto/cookies/cookies_instagram.json"):
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    try:
        load_cookies(driver, cookie_file)
        driver.get("https://www.instagram.com/")
        time.sleep(5)

        upload_button = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Nueva publicación']")
        upload_button.click()
        time.sleep(3)

        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(os.path.abspath(image_path))
        time.sleep(5)

        next_button = driver.find_element(By.XPATH, "//button[text()='Siguiente']")
        next_button.click()
        time.sleep(3)

        caption_area = driver.find_element(By.TAG_NAME, "textarea")
        caption_area.send_keys(caption)

        share_button = driver.find_element(By.XPATH, "//button[text()='Compartir']")
        share_button.click()
        time.sleep(5)

    finally:
        driver.quit()


if __name__ == "__main__":
    image_path = sys.argv[1]
    caption_file = sys.argv[2]
    with open(caption_file, "r") as f:
        caption = f.read().strip()
    post_image(image_path, caption)
