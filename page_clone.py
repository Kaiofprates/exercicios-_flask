
from flask import Flask
import os, requests, webbrowser
from tkinter import *
root = Tk()
root["bg"] = "#FF4500"
root.geometry("600x80")

def page ():
    link = end.get()
    x = requests.get(link)
    s = str(x.text)
    a = open("index.html","w")
    a.write(s)
    a.close()
    app = Flask(__name__)
    x = open("index.html","rb")
    s = x.read()
    @app.route("/")
    def hello_world():
        return s, 200
        #para linux
    os.system("gnome-terminal -- ./ngrok http 5000")
    webbrowser.open("http://localhost:5000/", autoraise=True)
    #para windows #os.system("ngrok http 5000")
    app.run()

end = Entry(root,bd = 4,width=50)
end.place(x=160,y=30)
butt = Button(root,text = "CLONAR", bd = 2,width = 10,command =page)
butt.place(x=30,y=29)

root.mainloop()
