import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://en.wikipedia.org/wiki/Saina_Nehwal"


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
print(curr)
first_p = soup.find("div",class_="mw-parser-output").find("p")

additional_info_1 = first_p.find_next_sibling("p").text.strip()

first_h2 = soup.find("div",class_="mw-parser-output").find("h2")
early_life = first_h2.find_next_sibling("p").text.strip()
learn = first_h2.find_next_sibling("p").find_next_sibling("p").find_next_sibling("p").text.strip()

start = learn.find("She trained under")
end = learn.find("train under Gopichand.") + len("train under Gopichand.")
desired = learn[start:end].strip()

x = infobox.find("th", string="Residence").find_next_sibling("td").text.strip()

home = ""
within_brackets = False
for i in x:
    if i == '[':
        within_brackets = True
    elif i == ']':
        within_brackets = False
        continue

    if not within_brackets:
        home += i

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

# home = ""
# for i in early_life:
#     if i == ',':
#         break
#     home = home+i
# home = home+'.'



first_h3 = soup.find("div",class_="mw-parser-output").find("h3")
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
ad = ad + "\n"+ ac
# get the coach
# coach = infobox.find("th", string="Coached by").find_next_sibling("td").text.strip()

# get the medal information
# medals = infobox.find("th", string="Medal record").find_next_sibling("td")
# medal_list = []
# for medal in medals.find_all("tr"):
#     medal_name = medal.find("td", {"class": "medaltable_victory_gold"}).text.strip()
#     medal_list.append(medal_name)

medal_count = 19
coach = "Pullela Gopichand"

# medal_record = infobox.find("th", string="Medal record")
# if medal_record:
#     # Find the next sibling of the medal record
#     sibling = medal_record.find_next_sibling()


#     while sibling and sibling.name != "h2":
#         if sibling.name == "table":
#             rows = sibling.find_all("tr")
        
#             medal_count += len(rows) - 1
        

#         sibling = sibling.find_next_sibling()


print("\n")
print("Name:", name)
print("Country:", country)
print("Birthdate:", birthdate)
print("Height:", ht)
print("Career:", career)
print("Highest Ranking:", h)
print("Current Ranking:", c)
print("Saina Nehwal has won", medal_count, "medals in her career.")
print("Coach:", coach)
# print("Medal Record:", ", ".join(medal_list))
print("\n")
print("Insight:  ", ad)
print("\n")
print("Early Life:  ", el)
print("\n")
print("Hometown: ",home)
print("\n")
print("Starting:  ",cs2)
print("\n")
print("Endorsemets:  ",endorsements)
print("\n")
print("Notable Achievements:  ", ac)
print("\n")
print("How she learnt:  ",desired)
print("\n")

# with sqlite3.connect("players.db") as con:
#     c = con.cursor()

#     c.execute(
#         "INSERT INTO playertables (Name, Country, Height,Career,  Medals, Coach, Insight, Early_Life, Hometown, Starting, Endorsements, Achievements, Learning,  Highest_Ranking, Birthdate, Current_Ranking) VALUES (?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)",
#         (name, country, ht, career,  medal_count, coach, ad, el, home, cs2, endorsements, ac, desired , h , birthdate,curr))

#     con.commit()
