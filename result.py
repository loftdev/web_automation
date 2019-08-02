from search import search_, driver

class Result:
    search_()

    def all_items(self):
        product_items = driver.find_elements_by_class_name('searchresultitem')
        counter = 0
        for i in product_items:
            counter += 1
            print(counter)
            print(i.find_element_by_class_name("title").text)
            print(i.find_element_by_class_name("price").text)
            print(""
                  "")
            if counter < 20:
                continue
            else:
                break
