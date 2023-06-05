import time
import urllib
import urllib.request
import urllib.parse
import os

from selenium import webdriver
 
 
def SelectUrl(purl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36'}
    ret = urllib.request.Request(purl, headers=headers)
    page = urllib.request.urlopen(ret, timeout=10)
    fileName = page.info()['Content-Disposition'].split('filename=')[1]
    fileName = fileName.replace('"', '').replace("'", "")
    logofile = page.read()
    fileName = "D:\\AllProject\\Python\\cosersets\\" + name + "\\" + work+ "\\" + fileName
    print(fileName)
    with open(fileName, "wb") as file:
        file.write(logofile)
 
 
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
 
        print(path + ' 创建成功')
 
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
 
        return False

proxy = "http://192.168.1.34:7890"
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=' + proxy)
driver = webdriver.Chrome(options=options)
 
url = "https://www.cosersets.com/1/main"
driver.get(url)
driver.implicitly_wait(30)
time.sleep(0.5)

name = ""
work = ""
from selenium.webdriver.common.by import By
NAME = driver.find_elements(By.CLASS_NAME, "el-table__row")
for i in range(0, len(NAME)):
    NAME = driver.find_elements(By.CLASS_NAME, "el-table__row")
    s = NAME[i].find_element(By.CLASS_NAME, "cell")
    name = s.text
    # print(s.text)
    driver.get(url + "/" + name)
    driver.implicitly_wait(30)
    time.sleep(3)
    WORK = driver.find_elements(By.CLASS_NAME, "el-table__row")
    for k in range(0, len(WORK)):
        WORK = driver.find_elements(By.CLASS_NAME, "el-table__row")
        s2 = WORK[k].find_element(By.CLASS_NAME, "cell")
        # print(s2.text)
        work = s2.text
        print(name + " | " + work)
        if work == "/":
            continue
        else:
            mkdir("D:\\AllProject\\Python\\cosersets\\" + name + "\\" + work)
            driver.get(url + "/" + name + "/" + work)
            driver.implicitly_wait(30)
            picture = driver.find_elements(By.CLASS_NAME, "img-mode-img")
            for j in range(0, len(picture)):
                print(picture[j].get_attribute("src"))
                r = picture[j].get_attribute("src")
                SelectUrl(r)
                #time.sleep(0.25)
 
        driver.get(url+ "/" + name)
        #driver.back()
        driver.implicitly_wait(30)
        time.sleep(3)
    driver.get(url)
    # driver.back()
    driver.implicitly_wait(30)
    time.sleep(3)
 
 
driver.quit()
