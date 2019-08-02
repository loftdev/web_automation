from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome(executable_path='/Users/loftymier/PycharmProjects/web_automation/chromedriver')
driver.get('https://www.lazada.sg/#')

timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "Level_1_Category_No1")))
except TimeoutException:
    driver.quit()

items = category_element = driver.find_element(By.ID,'Level_1_Category_No1').text
print(items)
#result -- Electronic Devices as the first category listing


list_category_elements = driver.find_element(By.XPATH,'//*[@id="J_icms-5000498-1511516689962"]/div/ul')
links = list_category_elements.find_elements(By.CLASS_NAME,"lzd-site-menu-root-item")
for i in range(len(links)):
    print("element in list ",links[i].text)
#result {Electronic Devices, Electronic Accessories, etc}

element = driver.find_elements_by_class_name('J_ChannelsLink')[1]
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()


product_titles = driver.find_elements_by_class_name('title')
for title in product_titles:
    print(title.text)
