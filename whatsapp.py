from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv
try:
    import autoit
except ModuleNotFoundError:
    pass
import os

msg = ""
with open('message.txt') as f:
    for text in f:
        msg += text

no_of_message = 1
recipetents_list = []
doc_filename = 'a.txt'

file_name = "numbers.csv"
try:
    csvfile = open(file_name, 'rt')
except:
    print("File not found")
csvReader = csv.reader(csvfile, delimiter=",")
for row in csvReader:
    recipetents_list.append(int((row[0])))
print(recipetents_list)


def element_presence(by, xpath, time):

    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():

    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except BaseException:
        is_connected()


driver = webdriver.Chrome()
driver.get("http://web.whatsapp.com")
sleep(10)


def send_files():
    clipButton = driver.find_element_by_xpath(
        '//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    sleep(1)
    docButton = driver.find_element_by_xpath(
        '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button')
    docButton.click()
    sleep(1)

    docPath = os.getcwd() + "\\Documents\\" + doc_filename

    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", (docPath))
    autoit.control_click("Open", "Button1")
    sleep(3)
    whatsapp_send_button = driver.find_element_by_xpath(
        # '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span'
        # '#app > div > div > div.YD4Yw > div._1-iDe.Wu52Z > span > div > span > div > div > div._2sNbV._3ySAH > span > div > div'
        '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
    whatsapp_send_button.click()
    if(element_presence(By.XPATH, '//*[@id="main"]/div[3]/div/div/div[2]/div[8]/div/div[1]/div/a/div/div[3]/span', 30)):
        continue
    else:
        sleep(10)


def send_whatsapp_msg(phone_no, text):

    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(
            phone_no)
    )

    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
            30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")
            if(doc_filename != 'NULL'):
                send_files()

    except Exception as e:
        print("Invailid phone no :" + str(phone_no))


def main():
    for moblie_no in recipetents_list:
        try:
            send_whatsapp_msg(phone_no=moblie_no, text=msg)

        except Exception as e:

            sleep(10)
            is_connected()


if __name__ == '__main__':
    main()
