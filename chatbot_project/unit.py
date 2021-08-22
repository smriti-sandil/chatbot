from chatterbot import ChatBot
bot=ChatBot("Unit",logic_adapters=[
    "chatterbot.logic.UnitConversion"
])
print("-----------++++------------------")
while True:
    user_text=   input("ask your question: ")
    print("Bot: "+str(bot.get_response(user_text)))