# class student:
#
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def show(self):
#         print(self.fname+" "+self.lname)
#
#
# class school(student):
#     def __init__(self,fname,lname,sclname):
#         super().__init__(fname,lname)
#         self.school=sclname
#         print(self.school+" "+self.fname)
#
#
#
# objs=[school("Sagar","Mishra","XLCR"),school("Samir","Mishra","XLCR")]
#
# for i in range(0,len(objs)):
#     print(objs[i].fname+" learns in "+objs[i].school)
#

#
# def algebraic(a,b,c):
#     return lambda x,y:a*x**2+b*y+c
#
# s=algebraic(1,2,3)
# print(s(1,2))

# import re
# user="User:{}"
# bot="Bot:{}"
#
# pattern="do you remember .*"
# data=input("Enter ques: ")
# print(user.format(data))
# if data.endswith("?"):
#     data=data.lower()
#     if re.search(pattern, data):
#         if "do" in data:
#             data=re.sub("do","Yes,",data)
#         if "you" in data:
#             data=re.sub("you","I",data)
#         if "my" in data:
#             data = re.sub("my", "your", data)
#         print(bot.format(data[0:len(data)-1:1]+"."))



# import random
#
# pinNumbers={}
#
#
# for i in range(1,11):
#     a=random.randint(1000,9999)
#     b=random.randint(1000,9999)
#     c=random.randint(1000,9999)
#     d=random.randint(1000,9999)
#     pinNumbers[str(a)+str(b)+str(c)+str(d)]=100
#     print(str(a)+" "+str(b)+" "+str(c)+" "+str(d))
#
#
# def confirmation():
#     ad = input("Provide y to continue: ")
#     ad.lower()
#     if ad == 'y':
#         userValue()
#     else:
#         exit()
#
#
# def userValue():
#     userCode=input("Enter your pin Code: ")
#     if userCode in pinNumbers.keys():
#         print("Successfully Recharged!!! "+str(pinNumbers[userCode]))
#         pinNumbers.pop(userCode)
#         confirmation()
#     else:
#         print("Invalid Code")
#         confirmation()
#
# for i in pinNumbers.keys():
#     print(i)
#
# userValue()
# from datetime import datetime
#
# b=datetime.now().strftime("%M")
# c=int(b)+5
#
# print(b)
# print(c)


# from passlib.hash import pbkdf2_sha256
#
# word="Sagar"
# word=word.lower()
# enc_password=pbkdf2_sha256.hash(word)
# print(type(enc_password))
#
# if pbkdf2_sha256.verify("sagar",enc_password):
#     print(True)
#
#
# class country:
#     world="Alien"
#     def __init__(self,cname,population):
#         self.cname=cname
#         self.population=population
#     @classmethod
#     def details(cls):
#         print("The world we are living in is surrounded by "+ cls.world)
#
#
#
#
# class citizen(country):
#     def __init__(self,cname,population,name,age):
#         super().__init__(cname,population)
#         self.name=name
#         self.age=age
#     def printDetails(self):
#         print("Hello my name is "+self.name+"\n I am "+str(self.age)+" years old."+"\n I am from "+self.cname)
#
#
# b=citizen("Nepal","2 millions","Sagar",20)
# b.printDetails()




