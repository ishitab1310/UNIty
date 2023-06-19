import requests
from bs4 import BeautifulSoup
import sqlite3

# define the wikipedia page url for PV Sindhu
url = "https://en.wikipedia.org/wiki/P._V._Sindhu"

# send a request to the page
response = requests.get(url)

# parse the html content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find the infobox table
infobox = soup.find(class_="infobox vcard")

# get the name
name = infobox.find("th", class_="infobox-above fn").text.strip()
# cou = infobox.find("th", class_ = "infobox-label")
# print(cou)
# while(1):
#     # print(cou)
#     country=''
#     if(cou == "):
#         country = infobox.find("td", class_="infobox-data").text.strip()
#         break
#     else:
#         cou = infobox.find("th", class_="infobox-label").find_next_sibling("th")
    
country = infobox.find("th", string="Country").find_next_sibling("td").text.strip()
# get the birthdate
birthdate = infobox.find("span", {"class": "bday"}).text.strip()
height = infobox.find("th", string="Height").find_next_sibling("td").text.strip()
ht=""
for i in height:
    if i==')':
        ht=ht+i
        break
    ht=ht+i
# # get the nationality
# nationality = infobox.find("th", string="Nationality").find_next_sibling("td").text.strip()

# # get the sport
# sport = infobox.find("th", string="Sport").find_next_sibling("td").text.strip()
career = infobox.find("th", string="Career record").find_next_sibling("td").text.strip()
high = infobox.find("th", string="Highest ranking").find_next_sibling("td").text.strip()
curr = infobox.find("th", string="Current ranking").find_next_sibling("td").text.strip()


h=""
for i in high:
    if i=='(':
        break
    h=h+i
c=""
for i in curr:
    if i=='(':
        break
    c=c+i

print("Name: ", name)
print("Country:",country)
print("Birthdate: ", birthdate)
print("Height:",ht)
# print("Nationality: ", nationality)
print("Career: ", career)
print("Highest Ranking:",h)
print("Current Ranking:",c)

with sqlite3.connect("players.db") as con:
    c = con.cursor()
    # c.execute("INSERT INTO playertable (name, Country, Height, career, curr) VALUES (?, ?, ?, ?, ?)",(name,country,ht,career,c))
    c.execute("CREATE TABLE playertable(Name varchar(50) not null, Country varchar(50) not null, Height varchar(50) not null, career varchar(50) not null, curr varchar(50) not null)")
    con.commit()
    con.close()


    
