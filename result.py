from search import driver, number_of_items
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def shorten_text(x):
    title_ = x["Title"]
    shorten_ = []

    for i in title_:
        shorten_.append(i[0:20] + "...")
    return shorten_


def filter_price(x):
    price_ = x["Price"]
    numbers = []

    for string in price_:
        numbers.append(int("".join(char for char in string if char.isdigit())))
    return numbers


class Result:

    def create_list(self):
        product_items = driver.find_elements_by_class_name('searchresultitem')
        counter = 0
        product_title = []
        product_price = []
        for i in product_items:
            counter += 1
            product_title.append(i.find_element_by_class_name("title").text)
            product_price.append(i.find_element(By.CLASS_NAME, "important").text)
            if counter < number_of_items:
                continue
            else:
                break
        data = {
            "Title": product_title,
            "Price": product_price
        }

        shorten_title = input('Enter "y" if you want to shorten title, "n" for full content: ').lower()
        shorten_price = input('Enter "y" if you want the price number only, "n" for full content: ').lower()

        if shorten_title == "y" and shorten_price == "y":
            data["Title"] = shorten_text(data)
            data["Price"] = filter_price(data)
            return data
        elif shorten_title == "y" and shorten_price == "n":
            data["Title"] = shorten_text(data)
            return data
        elif shorten_title == "n" and shorten_price == "y":
            data["Price"] = filter_price(data)
            return data
        else:
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
