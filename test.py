from page import *
try:
    with open("pages.json", "r") as f:
        pages = eval(f.read())
except FileNotFoundError: pass
print(pages)