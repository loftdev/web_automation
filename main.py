from search import search_
from export_csv import csv_call
from export_html import html_call


search_()
format_ = input('Format: '
                'Enter "c" for csv, '
                '"e" for excel, '
                '"h" for html: ').lower()


if format_ == "c":
    csv_call()
elif format_ == "e":
    pass
elif format_ == "h":
    html_call()
else:
    print(" You Entered the wrong format")
