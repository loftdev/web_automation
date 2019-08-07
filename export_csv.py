import pandas as pd
from result import Result
from search import sort


class ExportCsv:
    def standard(self):
        pd.DataFrame.from_dict(Result().standard()).to_csv('product_info.csv')

    def review(self):
        pd.DataFrame.from_dict(Result().review()).to_csv('product_info.csv')

    def cheap(self):
        pd.DataFrame.from_dict(Result().cheap()).to_csv('product_info.csv')

    def expensive(self):
        pd.DataFrame.from_dict(Result().expensive()).to_csv('product_info.csv')


def csv_call():
    if sort == "s":
        ExportCsv().standard()

    elif sort == "r":
        ExportCsv().review()
    elif sort == "c":
        ExportCsv().cheap()
    elif sort == "h":
        ExportCsv().expensive()
    else:
        print("You entered invalid letter")
