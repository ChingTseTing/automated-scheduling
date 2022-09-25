from selenium import webdriver



driverpath = "./chromedriver.exe"
browser = webdriver.Chrome(driverpath)
# browser = webdriver.Chrome('./chromedriver')


browser.get("https://zh.surveymonkey.com/r/EmployeeHealthDeclarationForm")
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
