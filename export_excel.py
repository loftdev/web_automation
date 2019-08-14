import pandas as pd
from result import Result
from search import sort


class ExportExcel:
    def standard(self):
        pd.DataFrame.from_dict(Result().standard()).to_excel('exported_folder/product_info.xls')

    def review(self):
        pd.DataFrame.from_dict(Result().review()).to_excel('exported_folder/product_info.xls')

    def cheap(self):
        pd.DataFrame.from_dict(Result().cheap()).to_excel('exported_folder/product_info.xls')

    def expensive(self):
        pd.DataFrame.from_dict(Result().expensive()).to_excel('exported_folder/product_info.xls')


def excel_call():
    if sort == "s":
        ExportExcel().standard()

    elif sort == "r":
        ExportExcel().review()
    elif sort == "c":
        ExportExcel().cheap()
    elif sort == "h":
        ExportExcel().expensive()
    else:
        print("You entered invalid letter")
