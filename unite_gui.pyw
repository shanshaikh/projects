#saved as .pyw to not show python console window

import requests
from bs4 import BeautifulSoup
import time
from tkinter import *
import datetime as dt

root = Tk()
root.title('Check last login time for Pokemon Unite')

name = Entry(root, width=50, borderwidth=5)
name.pack()

def getTime_S():
    url = 'http://www.uniteapi.dev/p/'
    name_v = name.get()
    url2 = url + name.get()
    r = requests.get(url2)
    if r.status_code != 200:
        label = Label(root, text="Invalid name: " + str(name_v))
        label.pack()
        return
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
    now = dt.datetime.now()
    final_t = dt.datetime.strptime(final, '%d-%m-%Y %H:%M')
    time_diff = now - final_t
    out_string = 'Name: ' + str(name_v) +' -> Last online: ' + \
                 str(final) + " :: " + str(time_diff.days) + " days"
    label = Label(root, text=out_string)
    label.pack()

button = Button(root, text="Submit Name", command=lambda: getTime_S())
button.pack()


root.mainloop()
