#!/usr/bin/python3
from flask import Flask

VERSION='0.1.0'

app = Flask(__name__)

@app.route('/')
def index():
    return "<html><div align='center'><br><h1>DEMO SNAP<br> v"+ str(VERSION) +"</h1></div></html>"

if __name__ == "__main__":                                                      
    app.run(host='0.0.0.0', port=8080, debug=True)
