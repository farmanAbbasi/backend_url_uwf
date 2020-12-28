from bs4 import BeautifulSoup
import requests
import os
from flask import Flask
from flask import request
app = Flask(__name__)
import json
from flask_cors import CORS, cross_origin
CORS(app)

BASE_URL=os.environ["base_url"]
def getMovieUrl(movieName):
    movieUrl=""
    url=BASE_URL+"/"+movieName
    res = requests.get(url)
    if res.status_code==200:
        html_content=requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        try:
            movieUrl=soup.find_all('iframe')[0]['src']
        except Exception as e:
            movieUrl=soup.find_all('tr')[1].find_all('a',href=True)
            for a in movieUrl:
                movieUrl=a['href']
        return movieUrl
    return movieUrl
            


@app.route('/loadData', methods=['GET'])
def loadData():
    name=request.args.get('name1')
    finalName=getMovieUrl(name)
    #if got the url 
    if(finalName!=""):
        return json.dumps({"url": finalName})
    return fileName

@app.route('/', methods=['GET'])
def getData():
    return json.dumps({"msg": "hello world from uwf"})

@app.route('/tmdb', methods=['GET'])
def getKeys():
    keys=os.environ['tmdb_keys']
    return json.dumps({"keys": keys})

#http://127.0.0.1:5000/loadData?name1=harry-potter-and-the-order-of-the-phoenix-2007-full-movie
if __name__ == '__main__':
    app.run()
    

    
        
