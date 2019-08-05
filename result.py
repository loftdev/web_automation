from search import search_, driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Result:

    def create_list(self):
        product_items = driver.find_elements_by_class_name('searchresultitem')
        counter = 0
        for i in product_items:
            counter += 1
            print(counter)
            print(i.find_element_by_class_name("title").text)
            print(i.find_element_by_class_name("price").text)
            print(""
                  "")
            if counter < 40:
                continue
            else:
                break

    def standard(self):
        Result().create_list()

    def review(self):
        sorting_category = Select(driver.find_element(By.CLASS_NAME, "sorting"))
        sorting_category.select_by_index(5)
        Result().create_list()

    def cheap(self):
        sorting_category = Select(driver.find_element(By.CLASS_NAME, "sorting"))
        sorting_category.select_by_index(1)
        Result().create_list()

    def expensive(self):
        sorting_category = Select(driver.find_element(By.CLASS_NAME, "sorting"))
        sorting_category.select_by_index(2)
        Result().create_list()

