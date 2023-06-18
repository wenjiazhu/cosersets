import time
import urllib.request
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

def select_url(purl, name, work):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36'
    }
    ret = urllib.request.Request(purl, headers=headers)

    try:
        page = urllib.request.urlopen(ret, timeout=30)
        file_name = purl.split('/')[-1]
        file_path = os.path.join("D:\\AllProject\\Python\\cosersets\\", name, work, file_name)
        print(file_path)
        if not os.path.exists(file_path):
            with open(file_path, "wb") as file:
                file.write(page.read())
                print(f"Downloaded file {file_name} successfully.")
        else:
            print(f"Skipping file {file_name} - File already exists.")
    except Exception as e:
        print(f"Error downloading file: {str(e)}")

def make_directory(path):
    path = path.strip().rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False

# proxy = "http://192.168.1.34:7890"
options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=' + proxy)
driver = webdriver.Chrome(options=options)

url = "https://www.cosersets.com/1/main"
driver.get(url)
driver.implicitly_wait(30)
time.sleep(3)

NAME = driver.find_elements(By.CLASS_NAME, "el-table__row")
for i in range(len(NAME)):
    NAME = driver.find_elements(By.CLASS_NAME, "el-table__row")
    s = NAME[i].find_element(By.CLASS_NAME, "cell")
    name = s.text
    driver.get(url + "/" + name)
    driver.implicitly_wait(30)
    time.sleep(3)

    time.sleep(3)  # 等待一段时间，确保页面加载完全
    WORK = driver.find_elements(By.CLASS_NAME, "el-table__row")
    for k in range(len(WORK)):
        WORK = driver.find_elements(By.CLASS_NAME, "el-table__row")
        if k >= len(WORK):
            continue
        s2 = WORK[k].find_element(By.CLASS_NAME, "cell")
        work = s2.text
        print(name + " | " + work)
        if work == "/":
            continue
        else:
            directory_path = os.path.join("D:\\AllProject\\Python\\cosersets\\", name, work)
            if os.path.exists(directory_path):
                print(f"Skipping directory {directory_path} - Directory already exists.")
                continue
            make_directory(directory_path)
            driver.get(url + "/" + name + "/" + work)
            driver.implicitly_wait(30)
            picture = driver.find_elements(By.CLASS_NAME, "img-mode-img")
            for j in range(len(picture)):
                r = picture[j].get_attribute("src")
                select_url(r, name, work)  # Pass name and work as arguments
                time.sleep(1)

        driver.get(url + "/" + name)
        driver.implicitly_wait(30)
        time.sleep(3)

    driver.get(url)
    driver.implicitly_wait(30)
    time.sleep(3)

driver.quit()
