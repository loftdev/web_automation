from search import search_
from export_csv import csv_call


search_()
format_ = input('Enter "c" for csv, '
                '"e" for excel, '
                '"h" for html: ').lower()


if format_ == "c":
    csv_call()
elif format_ == "e":
    pass
elif format_ == "h":
    pass
