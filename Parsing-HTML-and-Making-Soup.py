# Beautiful Soup Library
from bs4 import BeautifulSoup

# LXML Module
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# If above line doesn't work, then we have to add lxml parser instead
# soup = BeautifulSoup(contents, "lxml")


print(soup.title)
# Output: <title>Jawad's Personal Site</title>

print(soup.title.string)
# Output: Jawad's Personal Site

print(soup)
# This will print overall HTML text of a website

print(soup.prettify())
# This will print overall HTML text properly indented

print(soup.a)
# This will give us the first anchor tag that it finds in our website

print(soup.li)
# This will give us the first list tag that it finds in our website

print(soup.p)
# This will give us the first paragraph tag that it finds in our website

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# This will give us all the anchor tags that it finds in our website

all_paragraph_tags = soup.find_all(name="p")
print(all_paragraph_tags)
# This will give us all the paragraph tags that it finds in our website
