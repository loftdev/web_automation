from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/loftymier/PycharmProjects/web_automation/chromedriver")
driver.get('https://www.rakuten.co.jp')

keyword = input("Enter the item you want to search: ")

def search_():
    driver.find_element(By.ID, "sitem").click()
    driver.find_element(By.ID, "sitem").send_keys(keyword)
    driver.find_element(By.ID, "searchBtn").click()
    list_results = driver.find_elements(By.CLASS_NAME, "searchresultitems")
    return list_results
