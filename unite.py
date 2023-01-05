import requests
from bs4 import BeautifulSoup

url = 'http://www.uniteapi.dev/p/'
name = 'CrisHeroes' #change name here
url = url + name
r = requests.get(url)
val = BeautifulSoup(r.text, 'html.parser')
i = 0
for td in val.find_all("div"):
	if (i == 53):
		temp = str(td.find_next_sibling("p",class_="sc-7bda52f2-2 kUueIO"))
		break
	i+=1
	td.find_next_sibling("p",class_="sc-7bda52f2-2 kUueIO")
temp2 = temp.split('>')
final = temp2[2][0:-3]
print('Last online: ' + str(final))
