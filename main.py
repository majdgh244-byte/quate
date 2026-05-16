from requests import get
from bs4 import BeautifulSoup
from random import randint
while True:
 the_enter = input("عن ماذا تريد الاقتباس؟(تحفيز _ حياة _ تفاؤل _ خلط _ طموح) :")
 try:
   the_agin = int(input("ادخل عدد الاقتباسات :"))
 except ValueError:
   print("رجاء ادخل ارقاما في خانة عدد الاقتباسات")
   continue
 if the_enter == "خلط":
   y=0
   while the_agin>y:
     page = randint(1,190)
     majod = get("https://arabic-quotes.com/quotes" + "?page=" + str(page))
     html = majod.text
     x = BeautifulSoup(html,"html.parser")
     z = x.findAll("div",attrs={"class":"quote-container"})
     try:
       y = y + 1
       print(str(y)+z[randint(1,30)].text + "\n**************************************************************************************************")
     except IndexError:
         y = y-1
         page = randint(1,30)
 elif the_enter == "حياة":
   y=0
   while the_agin>y:
     page = randint(1,7)
     hayat = get("https://arabic-quotes.com/categories/14/%D8%AD%D9%8A%D8%A7%D8%A9" + "?page=" + str(page))
     html = hayat.text
     x = BeautifulSoup(html,"html.parser")
     z = x.findAll("div",attrs={"class":"quote-container"})
     try:
       y = y + 1
       print(str(y)+z[randint(1,30)].text + "\n**************************************************************************************************")
     except IndexError:
         y=y-1
         page = randint(1, 30)
 elif the_enter == "تفاؤل":
   y=0
   while the_agin>y:
     page = randint(1,3)
     tafaol = get("https://arabic-quotes.com/categories/5/%D8%AA%D9%81%D8%A7%D8%A4%D9%84-%D8%A3%D9%85%D9%80%D9%84" + "?page=" + str(page))
     html = tafaol.text
     x = BeautifulSoup(html, "html.parser")
     z = x.findAll("div", attrs={"class": "quote-container"})
     try:
       y = y + 1
       print(str(y)+z[randint(1, 30)].text + "\n*************************************************************************************************")
     except IndexError:
         y=y-1
         page = randint(1,30)
 elif the_enter == "تحفيز":
   y=0
   while the_agin>y:
     page = randint(1,10)
     tahfiz = get("https://arabic-quotes.com/categories/31/%D8%AA%D9%86%D9%85%D9%8A%D8%A9-%D8%A7%D9%84%D8%B0%D8%A7%D8%AA-%D8%AA%D8%AD%D9%81%D9%8A%D8%B2"+"?page="+str(page))
     html = tahfiz.text
     x = BeautifulSoup(html, "html.parser")
     z = x.findAll("div", attrs={"class": "quote-container"})
     try:
       y = y + 1
       print(str(y)+z[randint(1, 30)].text + "\n*************************************************************************************************")
     except IndexError:
         y=y-1
         page = randint(1, 30)
 elif the_enter == "طموح":
     y=0
     while the_agin > y:
       page = randint(1, 9)
       tahfiz = get("https://arabic-quotes.com/categories/9/%D8%B7%D9%85%D9%88%D8%AD-%D9%86%D8%AC%D8%A7%D8%AD" + "?page=" + str(page))
       html = tahfiz.text
       x = BeautifulSoup(html, "html.parser")
       z = x.findAll("div", attrs={"class": "quote-container"})
       try:
         y = y + 1
         print(str(y) + z[randint(1,30)].text + "\n*************************************************************************************************")
       except IndexError:
         y = y - 1
         page = randint(1, 30)
 else:
     print("رجاء ادخل نوع الاقتباس الصحيح(تحفيز _ حياة _ تفاؤل _ خلط _ طموح)\n")
     continue