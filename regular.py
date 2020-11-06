# import re
#
# bot="Bot: {}"
#
# sentence="Do you remember, you ate apple in garden?"
# pattern="Do you remember, .*"
# match=re.search(pattern,sentence)
#
# def response_rules(sentence):
#     message=sentence.lower()
#     if 'you' in message:
#         message=re.sub('you','I',message)
#
#     if 'do' in message:
#         message=re.sub('do','Yes',message)
#     if "?" in message:
#         message=message[0:len(message)-1:1]
#
#     return message
#
#
# if match:
#
#     print(bot.format(response_rules(sentence)))
# else:
#     print("Did not matched")


# import random
# list1=['Sagar','Samir','Kritika']
# print(random.choice(list1)

# # Chat bot
#
# import random
# import re
#
# user="User: {}"
# bot="Bot: {}"
#
#
# questionSet={
#     "hello":["Hi, How can we help you:)","Hello Sir, How can we help you:)"],
#     "my internet connection is very slow":["We appologize for that sir. And we are trying to fix it soon:)"],
#     "default":["Sorry for the delay, we would response as fast as possible:)","We would try to fix your problem soon!!!"]
# }
#
# def userQuestion():
#     question=input("Enter your question: ")
#     return question
#
#
# def response_pronouns(question):
#     question=question.lower()
#
#     pattern1="do you .*"
#     pattern2="what is .*"
#     pattern3="who are .*"
#     match1=re.search(pattern1,question)
#     match2=re.search(pattern2,question)
#     match3=re.search(pattern3,question)
#
#     if match1 or match2 or match3:
#         if "do" in question:
#             question=re.sub("do","Yes",question)
#         if "what" in question:
#             question=re.sub("what","Some problem",question)
#         if "who" in question:
#             question=re.sub("who","Anonymous User",question)
#         if "is" in question:
#             question=re.sub("is","has been",question)
#         if 'my' in question:
#             question = re.sub("my", " your", question)
#         if "i" in question:
#             question=re.sub("i","you",question)
#         if "am" in question:
#             question=re.sub("am","are",question)
#
#
#         print(bot.format(question[0:len(question)-1:1]+"."))
#     else:
#         print(bot.format("How can we help you?"))
#
#
# def respond(question):
#     question=question.lower()
#     if question in questionSet.keys():
#          print(bot.format(random.choice(questionSet[question])))
#     else:
#         print(bot.format(random.choice(questionSet["default"])))
#
# def send_response(question):
#     print(user.format(question))
#     if question.endswith("?"):
#         response_pronouns(question)
#         send_response(userQuestion())
#     else:
#         respond(question)
#         send_response(userQuestion())
#
#
# send_response(userQuestion())


# a=input("Enter a name to reverse: ")
# def reverse(a):
#     b=""
#     for i in range(len(a)-1,-1,-1):
#         b=b+a[i]
#     print(b.lower())

# list1=["pakistan","nepal","india","china"]
# list2=['pak','nep','ind','chn']
# print(list(filter(lambda x: len(x)>5,list1)))
# print(list(zip(list1,list2)))
#
# list2=[5,4,2,6,1,5]
# b=list(filter(lambda x: x>2,list2))
# print(b)
# print(list(map(lambda x: x**x,b)))

#
# import random
#
# numbers=[4,5,6,7,8,9]
# randomNumber=[]
#
# while len(randomNumber)!=len(numbers):
#     randomIndex=random.choice(numbers)
#
#     if randomNumber.__contains__(randomIndex):
#         pass
#     else:
#         randomNumber.append(randomIndex)
#
#
# for i in numbers:
#     print(i,end="\t")
#
# print()
#
# for i in randomNumber:
#     print(i,end="\t")
#


import re

# pattern="(\d\d\d\d\d\d\d\d\d\d)"
# user="User: {}"
# inputt=input("Enter your phone number: ")
#
# if len(inputt)>10 or len(inputt)<10:
#     print("invalid phone number")
#
# elif re.search(pattern,inputt):
#     print(user.format(inputt))
#
# else:
#     print("invalid phone number")


# pattern="do you remember .*"
# user="User: {}"
# bot="Bot: {}"
#
# def question():
#     userInput=input("Enter question: ")
#     return userInput
#
# def pronouns(question):
#     question=question.lower()
#     if re.search(pattern,question):
#         if "do" in question:
#             question=re.sub('do','Yes',question)
#         if "you" in question:
#             question=re.sub('you','I',question)
#         print(bot.format(question[0:len(question)-1]+"."))
#
#     else:
#         print(bot.format("Thank you for asking your queries!!"))
#
#
# def send_response(questions):
#     print(user.format(questions))
#     if questions.endswith("?"):
#         pronouns(questions)
#         send_response(question())
#     else:
#         print(bot.format("Thank you for asking queries!!"))
#
# send_response(question())
# from datetime import datetime, timezone, timedelta
#
# # a=datetime.now().strftime("%a-%B %I:%M %p")
# # print(a)
#
#
# a="2020-06-08"
# b=datetime.strptime(a,"%Y-%m-%d")
# print(b.strftime("%Y-%m-%d"))
# c="2:20 AM"
# # c=c[0:c.index(":")]+c[c.index(" "):len(c)]
# # print(c)
#
#
#
# if datetime.now().strftime("%Y-%m-%d") == a:
#     if c=="---":
#         print("Inappropriate date format!!")
#     elif c<datetime.now().strftime("%H:%M %p"):
#         print("Given time has already passed!!")
#     else:
#         print("Hurray")
# print(datetime.now().strftime("%H:%M %p"))
#
#
# class student:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#
#
#
#
# class school(student):
#     def __init__(self,schoolName,name,address):
#         super().__init__(name,address)
#         self.schoolName=schoolName
#
#     def prints(self):
#         print(self.name + " " + self.address+" "+self.schoolName)
#
# st=school("XLCR","Sagar","Swyambhu")
# st.prints()

#
# from passlib.hash import pbkdf2_sha256
#
#
# a="Sagar"
# b=pbkdf2_sha256.hash(a)
#
# use=input("Enter the letters: ")
# if(pbkdf2_sha256.verify(use,b)):
#     print(True)
#
# from datetime import datetime
# my_birthday="1999-12-13"
#
# year=datetime.now().year
# month=datetime.now().month
# day=datetime.now().day
# s=datetime.strptime(my_birthday,"%Y-%m-%d")
# birthYear=int(s.year)
# birthMonth=int(s.month)
# birthDay=int(s.day)
#
# def myage():
#     if month == birthMonth:
#         if day>birthDay:
#             print("You are " + str(year - birthYear ) + " years old.")
#         else:
#             print("You are " + str(year - birthYear-1) + " years old.")
#
#     elif month<birthMonth:
#         print("You are "+str(year-birthYear-1)+" years old.")
#     elif month>birthMonth:
#         print("You are " + str(year - birthYear) + " years old.")
#
# def myBday():
#     if month == birthMonth and day<birthDay:
#         print("After "+str(birthDay-day) +" days")
#     elif month<birthMonth:
#         print("After " + str(birthMonth - month) + " months")
#     elif month == birthMonth and day > birthDay:
#         print("After 12 months")
#     elif month>birthMonth:
#         print("After "+str(12-month)+" months")
#
# if month == birthMonth and day==birthDay:
#     print("Congratulations on getting "+str(year-birthYear)+" years old.")
# else:
#     myage()
#     myBday()
from datetime import datetime, timedelta

a="1999-6-28"
s=datetime.strptime(a,"%Y-%m-%d")
birthMonth=s.month
birthDay=s.day
d=s.replace(year=datetime.now().year)
e=s.replace(year=datetime.now().year+1)
print(e)
currentMonth=datetime.now().month
if birthMonth>currentMonth:
    print("Your birthday is after "+str(birthMonth-currentMonth)+" months.")
    print("Your birthday is after "+str((d-datetime.now()).days+1)+" days.")
elif currentMonth>birthMonth:
    print("Your birthday is after "+str(12-currentMonth+birthMonth)+" months")
    print("Your birthday is after " + str((e - datetime.now()).days+1) + " days.")
elif currentMonth == birthMonth:
    if birthDay>datetime.now().day:
        print("Your birthday is after " + str((d - datetime.now()).days+1) + " days.")
    elif birthDay == datetime.now() .day:
        print("Today is your birthday.")
    else:
        print("Your birthday is after " + str((e - datetime.now()).days+1) + " days.")







