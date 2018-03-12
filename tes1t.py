from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

#user = "leongmanchong@hotmail.com"
firstName = ""
lastName = ""
cityName = ""
chrome_path="/Users/manchongleong/Desktop/Taxonomy/chromedriver"
driver=webdriver.Chrome(chrome_path)
#fileName = ""
fileName = "/Users/manchongleong/Desktop/Crate/Geodata/US/National_Provider_Identifier/NPIDatabase_2015/NPPES_Data_Dissemination_July_2015/Original_state/State_USVI.csv"
data = pd.read_csv(fileName)[['Provider Last Name (Legal Name)','Provider First Name','Provider Business Mailing Address City Name']]
firstName = data['Provider First Name'].tolist()
lastName = data['Provider Last Name (Legal Name)'].tolist()
cityName = data['Provider Business Mailing Address City Name'].tolist()
driver.get("https://newjersey.mylicense.com/verification_4_6/Search.aspx?facility=N")
driver.maximize_window()
#driver.implicitly_wait(5)
#driver.switch_to.frame('fraPCSearch')
#assert "Facebook" in driver.title
#time.sleep(6)
elem = driver.find_element_by_id("t_web_lookup__first_name")
elem.send_keys(firstName[1])
elem = driver.find_element_by_id("t_web_lookup__last_name")
elem.send_keys(lastName[1])
elem = driver.find_element_by_id("t_web_lookup__addr_city")
elem.send_keys(cityName[1])

#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
#driver.close()


