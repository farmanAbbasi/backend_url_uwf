from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import request
app = Flask(__name__)
import json


BASE_URL="https://uwatchfree.mx"
def getMovieUrl(movieName):
    movieUrl=""
    url=BASE_URL+"/"+movieName
    res = requests.get(url)
    if res.status_code==200:
        html_content=requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        movieUrl=soup.find_all('iframe')[0]['src']
        return movieUrl
    return movieUrl
            


@app.route('/loadData', methods=['GET'])
def loadData():
    name=request.args.get('name1')
    finalName=getMovieUrl(name)
    #if got the url 
    if(finalName!=""):
        return json.dumps({"url": finalName})
    return ""

@app.route('/', methods=['GET'])
def getData():
    return json.dumps({"msg": "hello world from uwf"})
#http://127.0.0.1:5000/loadData?name1=harry-potter-and-the-order-of-the-phoenix-2007-full-movie
if __name__ == '__main__':
    app.run()
    

    
        
