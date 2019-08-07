from selenium import webdriver
from selenium.webdriver.common.by import By


keyword = input("Enter the item you want to search: ")
sort = input('Sorting By: '
             'Enter "r" for ratings, '
             '"c" for cheapest, '
             '"h" for expensive, '
             '"s" for standard: ').lower()
number_of_items = int(input("Enter the number of items from 1-40: "))

driver = webdriver.Chrome(executable_path="/Users/loftymier/PycharmProjects/web_automation/chromedriver")
driver.get('https://www.rakuten.co.jp')


def search_():
    driver.find_element(By.ID, "sitem").click()
    driver.find_element(By.ID, "sitem").send_keys(keyword)
    driver.find_element(By.ID, "searchBtn").click()
    list_results = driver.find_elements(By.CLASS_NAME, "searchresultitems")
    return list_results
