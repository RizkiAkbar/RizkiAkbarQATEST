from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# open web
driver = webdriver.Chrome()
current_page = 'http://kumparan.com'
success_page = 'http://kumparan.com'


driver.get(current_page)


#login pakai gmail
gmail = driver.find_element_by_xpath ('//button[@data-qa-id="btn-login-google"]')
gmail.click()


#try to wait 50s until new window popups
try:
	wait = WebDriverWait(driver, 50)
	wait.until(EC.number_of_windows_to_be(2))
except TimeoutException:
	self.fail( "Loading timeout expired" )

#isi login form sampe bisa login
login_success = 0

#get the url of second window popup
driver.switch_to_window(driver.window_handles[1])


email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
email_phone.send_keys("inputemailhererizkiakbar")

driver.find_element_by_id("identifierNext").click()
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)
password.send_keys("inputpasswordhererizkiakbar")
driver.find_element_by_id("passwordNext").click()

current_page = driver.current_url
self.assertEqual(
current_page,
success_page,
msg = "Successful Login"
)