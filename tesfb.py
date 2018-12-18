from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# open web
driver = webdriver.Chrome()
current_page = 'http://kumparan.com'
success_page = 'http://kumparan.com'

driver.get(current_page)

#login pakai facebook
fb_button = driver.find_element_by_xpath ('//button[@data-qa-id="btn-login-fb"]')
fb_button.click()

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

#get element of login form 
fb_email = driver.find_element_by_id ('email')
fb_pass = driver.find_element_by_id ('pass')
fb_submit = driver.find_element_by_id('u_0_0')

#input login form
email_user = 'inputemailhererizkiakbar'
pass_user = 'inputpasswordhererizkiakbar'

fb_email.send_keys(email_user)
fb_pass.send_keys(pass_user)

fb_submit.click()
wait = WebDriverWait(driver, 20)

error_elem = driver.find_element_by_xpath ('//div[@id="error_box"]')

#check element error exist
if error_elem.is_displayed():
	login_success = 0
	print('Login failed')
	exit()
else:
	login_success = 1

driver.switch_to_window(driver.window_handles[0])
wait = WebDriverWait(driver, 20)

#cek berhasil login
try:
	page_loaded = wait.until_not(
	lambda driver: driver.current_url == current_page
	)
except TimeoutException:
	self.fail( "Loading timeout expired" )

current_page = driver.current_url
self.assertEqual(
current_page,
success_page,
msg = "Successful Login"
)