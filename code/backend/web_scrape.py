from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('C:/Users/shrey/chromedriver/chromedriver.exe', options=options) 
page = ["","/udid/disability_details.html", "/udid/employment_details.html", "/udid/identitiy_details.html"]
f = open("questions.txt", "w")
for i in page:
    url = "https://capstonedemoudidform.herokuapp.com{}".format(i)
    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    for p1 in soup.find_all('tr'):
        if ("required" in str(p1) and "input" in str(p1)):
            if "radio" in str(p1):
                f.write("[radio] " + p1.text)
            else:
                f.write("[required] " + p1.text)
        elif "select" in str(p1):
           f.write("[choice] " + p1.text)
        else:
            if "checkbox" in str(p1):
                f.write("[checkbox] " + p1.text)
            else:
                f.write("[optional] " + p1.text)
        f.write("\n")
f.close()
driver.quit()

print("questions.txt generated")