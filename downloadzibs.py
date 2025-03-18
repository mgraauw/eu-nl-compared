# Use this url as page: https://decor.nictiz.nl/decor/services/ProjectIndex?prefix=zib2017bbr-&version=2021-10-29T11:39:09&format=html&language=nl-NL&ui=nl-NL
# Pirint all links in the "FHIR" column

import requests
from bs4 import BeautifulSoup
import os

format = "json"
language = "en-US"
base = "https://decor.nictiz.nl/decor/services/"
url = 'https://decor.nictiz.nl/decor/services/ProjectIndex?prefix=zib2020bbr-&format=html&ui=en-US' + '&language=' + language
# url = "https://decor.nictiz.nl/decor/services/ProjectIndex?prefix=demo1-"
# url = "https://decor.nictiz.nl/decor/services/ProjectIndex?prefix=zib2020bbr-&format=html&language=nl-NL&ui=nl-NL"
ziblist = ['nl.zorg.AllergyIntolerance', 'nl.zorg.Problem', 'nl.zorg.MedicalDevice', 'nl.zorg.HealthcareProvider', 'nl.zorg.Patient', 'nl.zorg.Procedure']

print(url)
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# # #transactionList
# table = soup.find("table", attrs={"id":"transactionList"}).tbody
# # print(table)
# for row in table.find_all("tr"):
#     cols = row.find_all("td")
#     if (cols[9].text == "Final"):
#         print(cols[10].text)
#         if(cols[10].text not in ziblist):
#             continue
#         anchors = cols[2].find_all("a")
#         for anchor in anchors:
#             if anchor.text == format:
#                 rt = requests.get(base + anchor['href'])
#                 name = cols[11].text.split('.')[-1] + '.' + format
#                 print(name)
#                 with open(os.path.join('zibs2020', name), 'wb') as f:
#                     f.write(rt.content)