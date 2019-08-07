from result import Result
from search import sort


class ExportHtml:

    def __init__(self):
        self.raw_data = None
        self.table_final = None

    def standard(self):
        self.raw_data = Result().standard()
        self.table_final = add_content(self.raw_data)
        convert_to_html(html_structure(self.table_final))

    def review(self):
        self.raw_data = Result().review()
        self.table_final = add_content(self.raw_data)
        convert_to_html(html_structure(self.table_final))

    def cheap(self):
        self.raw_data = Result().cheap()
        self.table_final = add_content(self.raw_data)
        convert_to_html(html_structure(self.table_final))

    def expensive(self):
        self.raw_data = Result().expensive()
        self.table_final = add_content(self.raw_data)
        convert_to_html(html_structure(self.table_final))


def add_content(data_result):
    table_ = "<table><tr><th>No.</th><th>Title</th><th>Price</th></tr>"
    title_ = data_result["Title"]
    price_ = data_result["Price"]
    counter = 0
    for i in range(len(title_)):
        table_ += f"<tr><td>{counter + 1}</td><td>{title_[counter]}</td><td>{price_[counter]}</td></tr>"
        counter += 1
    table_ += "</table>"
    return table_


def html_structure(table_final):
    return (f'<!DOCTYPE html>'
            f'<html lang="en">'
            f'<head><meta charset="UTF-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            f'<meta http-equiv="X-UA-Compatible" content="ie=edge">'
            f'<title>Document</title>'
            '<style> '
            'table, tr, td { '
            'border: 1px solid black'
            '}'
            f'</style>'
            f'</head>'
            f'<body> {table_final } </body>'
            f'</ html >')


def html_call():
    if sort == "s":
        ExportHtml().standard()

    elif sort == "r":
        ExportHtml().review()
    elif sort == "c":
        ExportHtml().cheap()
    elif sort == "h":
        ExportHtml().expensive()
    else:
        print("You entered invalid letter")


def convert_to_html(x):
    f = open("search_result.html", "w")

    f.write(x)
    f.close()
