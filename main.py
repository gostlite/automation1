from selenium import webdriver
from selenium.webdriver.common.by import By

path = "E:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://python.org")
# search_ = driver.find_element(by=By.NAME, value="q")
# pic = driver.find_element(by=By.CSS_SELECTOR, value=".python-logo")
# print(pic.get_attribute("src"))
# driver.get(link)
# print(search_.get_attribute("placeholder"))

Dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
Events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
print({num:{Dates[num].text, Events[num].text} for num in range(len(Dates))})

driver.quit()
