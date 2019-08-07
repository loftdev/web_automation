from search import driver, number_of_items
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Result:

    def create_list(self):
        product_items = driver.find_elements_by_class_name('searchresultitem')
        counter = 0
        product_title = []
        product_price = []
        for i in product_items:
            counter += 1
            product_title.append(i.find_element_by_class_name("title").text)
            product_price.append(i.find_element_by_class_name("price").text)
            if counter < number_of_items:
                continue
            else:
                break
        data = {
            "Title": product_title,
            "Price": product_price
        }

        return data

    def standard(self):
        return Result().create_list()

    def review(self):
        sorting_category = Select(driver.find_element(By.CLASS_NAME, "sorting"))
        sorting_category.select_by_index(5)
        return Result().create_list()

    def cheap(self):
        sorting_category = Select(driver.find_element(By.CLASS_NAME, "sorting"))
        sorting_category.select_by_index(1)
        return Result().create_list()

    def expensive(self):
        sorting_category = Select(driver.find_element(By.CLASS_NAME, "sorting"))
        sorting_category.select_by_index(2)
        return Result().create_list()
