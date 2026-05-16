from requests import get
from bs4 import BeautifulSoup
from random import randint
chois = input("enter the chois")
the_agin = int(input("enter the agin"))
majod = get("https://ar.wikiquote.org/wiki/%D8%A7%D9%84%D8%A3%D9%85%D9%84")
waad = get("https://ar.wikiquote.org/wiki/%D8%B4%D8%AC%D8%A7%D8%B9%D8%A9")
mohanad = get("https://ar.wikiquote.org/wiki/%D8%A7%D9%84%D8%B5%D8%AF%D8%A7%D9%82%D8%A9")
shjaa = waad.text
amal = majod.text
sadaqa = mohanad.text
amal_html = BeautifulSoup(amal,"html.parser")
shjaa_html = BeautifulSoup(shjaa,"html.parser")
sadaqa_html = BeautifulSoup(sadaqa,"html.parser")
amal_find = amal_html.findAll("li")
shjaa_find = shjaa_html.findAll("p")
shjaa_find_li = shjaa_html.findAll("li")
sadaqa_find = sadaqa_html.findAll("li")
print(sadaqa_find)
y = 0
while y < the_agin:
  n = randint(0, 40)
  if chois == "شجاعة":
    try:
      y = y + 1
      print(shjaa_find[n].text+"\n")
      print(shjaa_find_li[n].text)
    except IndexError:
      y = y - 1
      n = randint(0,40)
  elif chois == "امل":
      try:
          y = y + 1
          print(amal_find[n].text + "\n")
      except IndexError:
          y = y - 1
          n = randint(0,40)
  elif chois == "صداقة":
      try:
          y = y + 1
          print(sadaqa_find[n].text + "\n")
      except IndexError:
          y = y -1
          n = randint(0, 40)