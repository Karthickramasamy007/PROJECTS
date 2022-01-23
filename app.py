#This project is based on the example in the below link
#for more details see ReadMe-Karthick file
#https://docs.docker.com/language/python/build-images/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! v2'