import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://en.wikipedia.org/wiki/Srikanth_Kidambi"
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
h = infobox.find("th", string="Highest ranking").find_next_sibling("td").text.strip()
# h = ""
# for i in high:
#     if i == '(':
#         break
#     h = h + i

c = infobox.find("th", string="Current ranking").find_next_sibling("td").text.strip()
# c = ""
# for i in curr:
#     if i == '(':
#         break
#     c = c + i

first_p = soup.find("div", class_="mw-parser-output").find("p")
additional_info_1 = first_p.find_next_sibling("p").text.strip()

first_h2 = soup.find("div", class_="mw-parser-output").find("h2")
early_life = first_h2.find_next_sibling("p").text.strip()
# learn = first_h2.find_next_sibling("p").find_next_sibling("p").text.strip()

# start = learn.find("She first learned")
# end = learn.find("Gopichand Badminton Academy.") + len("Gopichand Badminton Academy.")
# desired = learn[start:end].strip()

    

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
x=0
desired = ""
for i in el:
    if x == 2:
        desired = desired +i
        
    elif i == '.' and x!= 2:
        x+=1
desired = desired +'.'

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
endorsements = "Information Not available"

achievements = soup.find("div", class_="mw-parser-output").find("h3").findNextSibling("h3").findNextSibling("h3").findNextSibling("h3").findNextSibling("h3")
ac1 = achievements
ac2 = achievements.findNextSibling("h3").findNextSibling("h3").find_next_sibling("p")
ac3= ac2.text.strip()
ac4 = ac2.find_next_sibling("h3").find_next_sibling("h3").find_next_sibling("h3").find_next_sibling("p").text.strip()
ac6=""
for i in ac3:
    if i == '.':
        break
    #     within_brackets = True
    # elif i == ']':
    #     within_brackets = False
    #     continue
    # if not within_brackets:
    ac6 = ac6+ i
ac6 = ac6+'.'
ac5=""
# # within_brackets = False
for i in ac4:
    if i == '.':
        break
    #     within_brackets = True
    # elif i == ']':
    #     within_brackets = False
    #     continue
    # if not within_brackets:
    ac5 = ac5+ i
ac5 = ac5+'.'
ac7 = ac6 + " " + ac5





# achievements_2 = soup.find("div", class_="mw-parser-output").find("p").find_next_sibling("p").find_next_sibling("p").find_next_sibling("p").text.strip()
# ac2 = ""
# within_brackets = False
# for i in achievements_2:
#     if i == '[':
#         within_brackets = True
#     elif i == ']':
#         within_brackets = False
#         continue
#     if not within_brackets:
#         ac2 += i
# ac = ac + "\n" + ac2
# ad = ad + "\n" + ac

medal_count = 14
coach = "Wiempie Mahardi"

# print("\n")
# print("Name:", name)
# print("Country:", country)
# print("Birthdate:", birthdate)
# print("Height:", ht)
# print("Career:", career)
# print("Highest Ranking:", h)
print("Current Ranking:", c)
# print("Kidambi Srikanth has won", medal_count, "medals in his career.")
# print("Coach:", coach)
# # print("Medal Record:", ", ".join(medal_list))
# print("\n")
# print("Early Life:  ", el)
# print("\n")
# print("Insight:  ", ad)
# print("\n")
# print("Hometown: ",home)
# print("\n")
# print("Starting:  ",cs2)
# print("\n")
# print("Endorsemets:  ",endorsements)
# print("\n")
# print("Notable Achievements:  ", ac7)
# print("\n")
# print("How he learnt:  ",desired)
# print("\n")

# with sqlite3.connect("players.db") as con:
#     c = con.cursor()

#     c.execute(
#         "INSERT INTO playertables (Name, Country, Height,Career,  Medals, Coach, Insight, Early_Life, Hometown, Starting, Endorsements, Achievements, Learning,  Highest_Ranking, Birthdate) VALUES (?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)",
#         (name, country, ht, career,  medal_count, coach, ad, el, home, cs2, endorsements, ac7, desired , h , birthdate))

#     con.commit()
