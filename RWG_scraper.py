from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# options = Options()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("detach", True)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=options)
driver.get("https://randomwordgenerator.com/")

print(driver.title)

def Search_words():
    dict = []

    for i in range(2):

        Id_intializer = i+1

        search = driver.find_element(By.ID,"qty").clear()
        search = driver.find_element(By.ID,"qty").send_keys("50" + Keys.ENTER)

        time.sleep(5)

        String_word = ""
        mainEle = driver.find_element(By.ID,"result")
        results = mainEle.find_elements(By.TAG_NAME,"li")
        for result in results:
            # dict.update({Id_intializer:result.text})
            # Id_intializer+=1
            String_word+=result.text
            String_word+='_'

        print(f'#{i+1}...............')
        dict1 = {
            "id": Id_intializer,
            "words": String_word
        }
        
        dict.append(dict1)
        # print(dict)
        # print(String_word)

    with open("test1.json","w") as testFile:
        json.dump(dict,testFile)

Search_words()
# Search_words()

driver.quit()    


