from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
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

    
driver = webdriver.Chrome(options = chrome_options)
#browser = webdriver.Chrome('./chromedriver/chromedriver.exe')


driver.get("https://zh.surveymonkey.com/r/EmployeeHealthDeclarationForm")
email = browser.find_element("id", "66722352")
email.send_keys('138516')

##
browser.find_element("id", "66722353_544681771_label").click()
browser.find_element("id", "66722351_544681761_label").click()
browser.find_element("xpath","//button[@type='submit']").click()

##
browser.find_element("id", "66722354_544681783_label").click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()

##
browser.find_element("id", "66722361_544681835_label").click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()
##
browser.find_element("id", "66722355_544681787_label").click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()

##
browser.find_element("id", "66722366_544681859_label").click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()

##
browser.find_element("id", "66722356_544681790").click()
browser.find_element("xpath","//button[@class='btn small done-button survey-page-button user-generated notranslate']").click()


#####
browser.get("https://zh.surveymonkey.com/r/EmployeeHealthCheck")

browser.find_element("id", "87960815_688357155_label").click()
email = browser.find_element("id", "87960813")
email.send_keys('138516')
browser.find_element("id", "87960820_688357202_label").click()
browser.find_element("id", "87960821_688357189_label").click()

email2= browser.find_element("id", "87960822_688357192_DMY")
email2.send_keys('09/13/2022')
browser.find_element("id", "87960814_688357154_label").click()
browser.find_element("xpath","//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()
