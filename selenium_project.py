from selenium import webdriver

chromedriver = "/home/terry/Desktop/projects/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http://google.com")