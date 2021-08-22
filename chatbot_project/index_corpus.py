from chatterbot import ChatBot
import chatterbot
import requests
from flask import Flask, render_template,request
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import logging

from flask.wrappers import Request
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

app = Flask(__name__)

bot = ChatBot("SmBot",read_only= False,
logic_adapters =[
    
    {"import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I don't have an answer",
    "maximum_similarity_threshold": 0.9
    }
    ])

# trainer =  ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.english')

@app.route("/")
def main():
    return render_template("index.html")

# while True:

#     user_response=input("User: ")
#     print("SmBot: ",bot.get_response(user_response))
@app.route('/get')
def get_chatbot_response():
    userText=request.args.get('usermessage')
    raw_data= requests.get("http://api.openweathermap.org/data/2.5/weather?q="+userText+"&appid=b3eb85913c29ec06f700f18a8f6468ad")
    result=raw_data.json()
    return result
    

if __name__ == "__main__":
    app.run(debug=True)