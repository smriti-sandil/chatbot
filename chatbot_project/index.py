from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

bot = ChatBot("SmBot",read_only= False, 
logic_adapters =[
    
    {"import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I don't have an answer",
    "maximum_similarity_threshold": 0.9
    }
    ])
list_train1=[
            "Hi",
            "Hello master!, how can I help you?",
            "what is your name ?",
            "I am SmBot",
            "How old are you ?",
            "I am ageless",
            "How was the day?",
            "Nice Day",    
            "what is your fav work? ",
            "Talking to you master",
            "I do't know what you are talking about"
]

list_train2=[
            "Hi",
            "Hello Sir!, how can I help you?",
            "what is your name ?",
            "I am Smbot2",
            "How old are you ?",
            "I am ageless",
            "How was the day?",
            "Good Day",    
            "what is your fav work? ",
            "Talking to you Sir",
            "I don't know what you are talking about"
]
list_trainer = ListTrainer(bot)
list_trainer.train(list_train1)
list_trainer.train(list_train2)
while True:

    user_response=input("User: ")
    print("SmBot: ",bot.get_response(user_response))

