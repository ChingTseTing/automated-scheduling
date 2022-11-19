from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from datetime import datetime

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
browser = webdriver.Chrome(options = chrome_options)
#browser = webdriver.Chrome('./chromedriver/chromedriver.exe')

browser.get("https://zh.surveymonkey.com/r/EmployeeHealthDeclarationForm")
email = browser.find_element("xpath","//input[@class='wds-input wds-input--lg qt-input_text text']")
email.send_keys('138516')


##
browser.find_elements("xpath","//label[@class='answer-label radio-button-label no-touch touch-sensitive clearfix']")[0].click()  # 同上
browser.find_elements("xpath","//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[2].click()  # 同上
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()


#
browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[1].click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()

#               
browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[1].click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()

#
browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[1].click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()

##
browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[1].click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()


##

browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[0].click()
browser.find_element("xpath","//button[@class='btn small done-button survey-page-button user-generated notranslate']").click()


#####
browser.get("https://zh.surveymonkey.com/r/EmployeeHealthCheck")
browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[0].click()
email = browser.find_elements("xpath", "//input[@class='wds-input wds-input--lg qt-input_text text']")[0]
email.send_keys('138516')

         
browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[4].click()

browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[8].click()

email2= browser.find_element("xpath", "//input[@class='form-control text date--picker date-validation']")
email2.send_keys(datetime.now().strftime("%m/%d/%Y"))  

browser.find_elements("xpath", "//span[@class='radio-button-label-text question-body-font-theme user-generated ']")[9].click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()
