import os, sys, time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def load_cookies(driver, cookie_file):
    driver.get("https://www.tiktok.com/")
    with open(cookie_file, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(5)


def post_video(video_path, caption, cookie_file="/root/proyectos/social_auto/cookies/cookies_tiktok.json"):
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    try:
        load_cookies(driver, cookie_file)
        driver.get("https://www.tiktok.com/upload")
        time.sleep(5)

        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(os.path.abspath(video_path))
        time.sleep(10)

        caption_area = driver.find_element(By.XPATH, "//div[@role='textbox']")
        caption_area.send_keys(caption)
        time.sleep(2)

        post_button = driver.find_element(By.XPATH, "//button[contains(text(),'Publicar')]")
        post_button.click()
        time.sleep(10)

    finally:
        driver.quit()


if __name__ == "__main__":
    video_path = sys.argv[1]
    caption_file = sys.argv[2]
    with open(caption_file, "r") as f:
        caption = f.read().strip()
    post_video(video_path, caption)
