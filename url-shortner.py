""" pip install pyshorteners
pip install pyperclip
"""

import pyperclip
import pyshorteners
from tkinter import *

root=Tk()
root.geometry("400x300")
root.title("Puneet's URL SHORTNER")
root.configure(bg="orange")
url= StringVar()
url_address = StringVar()

def urlshortner():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short= url_address.get()
    pyperclip.copy(url_short)

Label(root,text="Puneet's URL Shortener", font="poppins",bg="black",fg="orange").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortner,bg="black",fg="orange",width=15, height=1).pack(pady=7)
Entry(root,textvariable=url_address).pack(pady=5)
Button(root, text="Copy Short URL", command=copyurl,bg="black",fg="orange",width=15, height=1 ).pack(pady=7)

root.mainloop()
