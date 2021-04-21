from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.google.com')
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("Yahoo")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()