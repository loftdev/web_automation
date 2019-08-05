from result import Result
from search import search_, sort


search_()

if sort == "s":
    Result().standard()
elif sort == "r":
    Result().review()
elif sort == "c":
    Result().cheap()
else:
    print("You entered invalid letter")
