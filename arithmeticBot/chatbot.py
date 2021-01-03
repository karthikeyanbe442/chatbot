from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('ArithmeticBot',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation', 
            'chatterbot.logic.BestMatch'
        ])

trainer = ListTrainer(bot)

trainer.train([
    "Hi.",
    "Hello Human! What can I do for you?",
    "What can you do?",
    "My skill level is limited to arithemtic operations"])

username=input("\nChatbot is ready! \nWhat is your name? : ")

while True:
    try:
        msgFromUser=input("{}: ".format(username))
        if(msgFromUser.lower() == 'bye'):
            print("Bot: Bye")
            break

        msgFromBot=bot.get_response(msgFromUser)
        print("Bot: {}".format(msgFromBot))
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("Bot: Bye")
        break
    except:
        print("Bot: Sorry could not understand.")

