from flask import Flask
import os
import requests

link = raw_input("link: ")
x = requests.get(link)
s = str(x.content)
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


app.run()

