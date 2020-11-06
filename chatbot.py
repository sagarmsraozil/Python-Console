import re
import random

user="User:{}"
bot="Bot:{}"




def askQuestion():
    question=input("User:")
    return question


# intent

userQuestion={
    "hello":["Hello, It's nice to meet you!!","Hi, It's pleasure meeting you!!","Welcome to chatbot arena!!"],
    "i am having problem":["We are trying to identify your problem. Can you give us little more detail about the problem?"],
    "my internet is slow":["We are trying to fix your issue. Please switch off your wifi for 5 minutes a day."],
    "who are you":["I am Mr. Chatbot","You can call me Beast"],
    "how are you":["I am fine, wbu?"],
    "i am good":["It seems to be a good day for you:)","Wow that's nice!"],
    "what is my name":["You are my sweet user!!"],
    "what's my name":["You are my sweet user!!"],
    "who am i":["You are my sweet user!!"],
    "help":["How can I help you?"],
    "Default":"Thank you for concerning. Our technical persons are busy right now. We would contact you as soon as they return!"
}

def reply_intent(question):
    if question.endswith('.') or question.endswith('!') or question.endswith(':)') or question.endswith('?'):
        question=question[0:len(question)-1:1]

        reply_intent(question)
    else:
        if question in userQuestion.keys():
            print(bot.format(random.choice(userQuestion[question])))
        else:
            print(bot.format(userQuestion["Default"]))


def pronouns_checker(question):
    pattern1="do you .*"

    if re.search(pattern1,question):
        if 'do' in question:
            question=re.sub('do','Yes',question)
        if 'you' in question:
            question=re.sub('you','I',question)
        if 'my' in question:
            question=re.sub('my','your',question)
        if 'am' in question:
            question = re.sub('am', 'are', question)
        if ' i ' in question:
            question = re.sub(' i ', 'you', question)
        if 'me' in question:
            question = re.sub('me', 'you', question)
        print(bot.format(question[0:len(question) - 1:1] + "."))
    else:
       reply_intent(question)



def reply(question):

    userQuestion=question.lower()
    if userQuestion.endswith('?'):
        pronouns_checker(userQuestion)
        reply(askQuestion())
    else:
        reply_intent(userQuestion)
        reply(askQuestion())



reply(askQuestion())



