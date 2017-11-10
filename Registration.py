from  selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

driver = webdriver.Firefox()
wait = WebDriverWait(driver,5)
driver.get('http://5.100.252.15/app/#OpenAccount')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="titleId"]').click()
driver.find_element_by_xpath('//*[@id="titleId"]/option[2]').click()

first_name = 'Nataly'
last_name = "Beresn"
tel = '1239887'
email = 'mail@mail1.com'
driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys(first_name)
driver.find_element(By.XPATH,'//*[@id="lastName"]').send_keys(last_name)
driver.find_element(By.XPATH,'//*[@id="phoneNumber"]/input[2]').send_keys(tel)
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(email)
#Set date of birth
driver.find_element(By.XPATH, '//*[@id="birthDate"]/select[1]').click()
driver.find_element(By.XPATH, '//*[@id="birthDate"]/select[1]/option[21]').click()

driver.find_element(By.XPATH, '//*[@id="birthDate"]/select[2]').click()
driver.find_element(By.XPATH, '//*[@id="birthDate"]/select[2]/option[13]').click()

driver.find_element(By.XPATH, '//*[@id="birthDate"]/select[3]').click()
driver.find_element(By.XPATH, '//*[@id="birthDate"]/select[3]/option[17]').click()

user = 'user1983'
passw = '111111'
passw2 = passw

driver.find_element(By.XPATH,'//*[@id="userName"]').send_keys(user)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(passw)
driver.find_element(By.XPATH,'//*[@id="retypePassword"]').send_keys(passw2)

code = 12233

driver.find_element(By.XPATH,'//*[@id="captcha"]').send_keys(code)

driver.find_element(By.XPATH,'//*[@id="confirmAge"]').click()

driver.find_element(By.XPATH,'//*[@id="application"]/div/div[2]/div/div/div/div[3]/div[1]/i').click()


