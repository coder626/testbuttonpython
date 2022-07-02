from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import mysql.connector
from mysql.connector.constants import ClientFlag
import tkinter as tk
from tkinter import *
import time


#creates the webdriver
driver = webdriver.Chrome(executable_path='/Users/edwardlavelle/Downloads/chromedriver')

#NOTE: Chromedriver now works!!!!

#go to CMU website
driver.get("https://academy.cs.cmu.edu/login")

#maximize the window and wait so everything can be formatted into the screen
driver.maximize_window()
time.sleep(3)

#find the username and password elements by HTML ID
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

#send the keys 
username.send_keys("coder626")
password.send_keys("Password1")


#button = driver.find_element_by_class_name('flat span aquamarine')

#button = driver.find_element_by_id("Log in")

#button = driver.find_element_by_link_text('Log in')

#button = driver.find_element_by_css_selector('button.flat.span.aquamarine')

#button = driver.find_element("flat.span.aquamarine")

#next series of statements just finds buttons and clicks them to get to the code history
button = driver.find_element(By.CSS_SELECTOR, '[class="flat span aquamarine"]')
button.click()

driver.get("https://academy.cs.cmu.edu/ide")

dropDownMenu = driver.find_element_by_id('file-operations-dropdown')

dropDownMenu.click()

openButton = driver.find_element_by_link_text('Open')

openButton.click()

#wait and allow CMU backend process to complete
time.sleep(2)

#click some buttons just as a user would
bubbleSortFile = driver.find_element(By.CSS_SELECTOR, '[class="file-name-only"]')

bubbleSortFile.click()

#selectAllButton = driver.find_element(By.CSS_SELECTOR, '[class="icon select-all"]')

#selectAllButton.click()

aceContent = driver.find_element(By.CSS_SELECTOR, '[class="ace_content"]')

aceContent.click()


#process for Selenium copy and paste
# action chain object creation
action = ActionChains(driver)
# perform the ctrl+c pressing action
           
action.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.CONTROL).perform()
action.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.CONTROL).perform()
root = tk.Tk()
#print(root.clipboard_get())

#Google Cloud configuration
config = {
    'user': 'root',
    'password': 'Password123',
    'host': '34.94.63.132',
    'database': 'BubbleSortFiles'
    #'client_flags': [ClientFlag.SSL],
    #'ssl_ca': 'ssl/server-ca.pem',
    #'ssl_cert': 'ssl/client-cert.pem',
    #'ssl_key': 'ssl/client-key.pem'
}

#Google Cloud config simplified
mydb = mysql.connector.connect(
  host="34.94.63.132",
  user="root",
  password="Password123",
  database="BubbleSortFiles"
)

#create an SQL cursor
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE codefiles (filename VARCHAR(255), code VARCHAR(5000))")


#print(root)


#SQL INSERT
sql = "INSERT INTO codefiles (filename, code) VALUES (%s, %s)"
rootString = StringVar()
rootString = root.clipboard_get()
#print(root)
val = ("file1", rootString)

#print(rootString)


#mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")




