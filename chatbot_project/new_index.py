from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

bot = ChatBot("SBot",read_only= False,
logic_adapters =[
    
    {"import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I don't have an answer",
    "maximum_similarity_threshold": 0.9
    }
    ])
    
list = [
    "Hi",
    "Hello, there",
    "what are the services you have?",
    "please go to this url for more info https://internshala.com ",
    "what is your contact page?",
    "visit this link  https://internshala.com/contact"
]

list_train = ListTrainer(bot)

list_train.train(list)
while True:

    user_response=input("User: ")
    print("Bot: ",bot.get_response(user_response))