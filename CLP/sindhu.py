import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://en.wikipedia.org/wiki/P._V._Sindhu"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
infobox = soup.find(class_="infobox vcard")

name = infobox.find("th", class_="infobox-above fn").text.strip()
country = infobox.find("th", string="Country").find_next_sibling("td").text.strip()
birthdate = infobox.find("span", {"class": "bday"}).text.strip()
height = infobox.find("th", string="Height").find_next_sibling("td").text.strip()
ht = ""
for i in height:
    if i == ')':
        ht = ht + i
        break
    ht = ht + i

career = infobox.find("th", string="Career record").find_next_sibling("td").text.strip()
high = infobox.find("th", string="Highest ranking").find_next_sibling("td").text.strip()
h = ""
for i in high:
    if i == '(':
        break
    h = h + i

curr = infobox.find("th", string="Current ranking").find_next_sibling("td").text.strip()
c = ""
for i in curr:
    if i == '(':
        break
    c = c + i

first_p = soup.find("div", class_="mw-parser-output").find("p")
additional_info_1 = first_p.find_next_sibling("p").text.strip()

first_h2 = soup.find("div", class_="mw-parser-output").find("h2")
early_life = first_h2.find_next_sibling("p").text.strip()
learn = first_h2.find_next_sibling("p").find_next_sibling("p").text.strip()

start = learn.find("She first learned")
end = learn.find("Gopichand Badminton Academy.") + len("Gopichand Badminton Academy.")
desired = learn[start:end].strip()

ad = ""
within_brackets = False
for i in additional_info_1:
    if i == '[':
        within_brackets = True
    elif i == ']':
        within_brackets = False
        continue
    if not within_brackets:
        ad += i

el = ""
within_brackets = False
for i in early_life:
    if i == '[':
        within_brackets = True
    elif i == ']':
        within_brackets = False
        continue
    if not within_brackets:
        el += i

home = ""
for i in early_life:
    if i == ',':
        break
    home = home + i
home = home + '.'

first_h3 = soup.find("div", class_="mw-parser-output").find("h3")
cs = first_h3.find_next_sibling("p").text.strip()
cs2 = ""
within_brackets = False
for i in cs:
    if i == '[':
        within_brackets = True
    elif i == ']':
        within_brackets = False
        continue
    if not within_brackets:
        cs2 += i

second_h2 = first_h2.find_next_sibling("h2").find_next_sibling("h2")
endorsements = second_h2.find_next_sibling("p").find_next_sibling("p").text.strip()

achievements = soup.find("div", class_="mw-parser-output").find("p").find_next_sibling("p").find_next_sibling("p").text.strip()
ac = ""
within_brackets = False
for i in achievements:
    if i == '[':
        within_brackets = True
    elif i == ']':
        within_brackets = False
        continue
    if not within_brackets:
        ac += i

achievements_2 = soup.find("div", class_="mw-parser-output").find("p").find_next_sibling("p").find_next_sibling("p").find_next_sibling("p").text.strip()
ac2 = ""
within_brackets = False
for i in achievements_2:
    if i == '[':
        within_brackets = True
    elif i == ']':
        within_brackets = False
        continue
    if not within_brackets:
        ac2 += i
ac = ac + "\n" + ac2
ad = ad + "\n" + ac

medal_count = 25
coach = "Pullela Gopichand"

with sqlite3.connect("players.db") as con:
    c = con.cursor()

    c.execute(
        "INSERT INTO playertables (Name, Country, Height,Career,  Medals, Coach, Insight, Early_Life, Hometown, Starting, Endorsements, Achievements, Learning,  Highest_Ranking, Birthdate, Current_Ranking) VALUES (?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)",
        (name, country, ht, career,  medal_count, coach, ad, el, home, cs2, endorsements, ac, desired , h , birthdate,curr))

    con.commit()
