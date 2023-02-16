import json
from flask import Flask, render_template, request
import requests
import datetime


x = datetime.datetime.now()

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
    print(flask.__version__) # Print the module verison
    
    
def getRandMemes(nbrMemes):
    url = f'https://meme-api.com/gimme/{nbrMemes}'
    memes = json.loads(requests.get(url).text)
    # memes = response.json()
    return memes

def getSubReddMemes(subRedd, nbrMemes):
    url = f'https://meme-api.com/gimme/{subRedd}/{nbrMemes}'
    memes = json.loads(requests.get(url).text)
    return memes

@app.route('/randMemes')
def input():
    memes = getRandMemes(50)
    return render_template('index.html', memes=memes)
    # return memes
   

@app.route('/<subRedd>')
def subRedd(subRedd):
    memes = getSubReddMemes(subRedd, 50)
    return render_template('index.html', memes=memes)
    # return memes


