from chatterbot import ChatBot
bot=ChatBot("Math",logic_adapters=[
    "chatterbot.logic.MathematicalEvaluation"
])
print("-----------++++------------------")
while True:
    user_text=   input("type your math equation that you want to solve: ")
    print("Bot: "+str(bot.get_response(user_text)))