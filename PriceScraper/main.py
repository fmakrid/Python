from bs4 import BeautifulSoup
import requests

print("Paste the link")

url = input()

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

prices = soup.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
weak = parent.find("sup")

total = strong.string + weak.string

f= open("prices.txt","w+")
f.write(total)
f.close()

print(total)
