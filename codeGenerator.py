# from datetime import datetime
#
# a="1999-07-13"
# a=datetime.strptime(a,"%Y-%m-%d")
# b=a.replace(year=datetime.now().year)
# print(b.strftime("%Y-%m-%d"))
# c=datetime.now()
#
# if c.month>a.month:
#     years=int((b-a).days/365)
# elif c.month<a.month:
#     years=int((b-a).days/365)-1
# else:
#     if c.day>a.day:
#         years = int((b - a).days / 365)
#     else:
#         years = int((b - a).days / 365) - 1
#
#
# print(str(years)+" years")

#
# class Student:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#
#
#     def multiply(self):
#         a=self.age
#
#         for i in range(1,a+1):
#             c=0
#             for j in range(1,i+1):
#                 if(i%j==0):
#                     c+=1
#             if c==2:
#                 print(f'{i} is prime number')
#             else:
#                 print(f'{i} is composite number')
#
#
# class newClass(Student):
#     def __init__(self,fname,lname,age):
#         super().__init__(fname,lname,age)
#
#
#
# d=newClass("Sagar","Mishra",20)
# d.multiply()

#
# import random
# import re
#
# myDictionary={
#     "what is your name":["My name is Chappie","It's me Chappie","You can call me, Chappie"],
#     "how old are you":["I am 4 yrs old",'4 yrs old','4 yrs and growing'],
#     "how are you":['I am fine','All good','Fresh!!'],
#     "lets go for date":['I am busy person','Lots of task to do'],
#     "Default":['We would reply you sooner']
# }
#
#
# def questions():
#     a=input("Ask:")
#     return a
# bot="Bot:{0}"
#
# def response(a):
#     if a in myDictionary.keys():
#         print(bot.format(random.choice(myDictionary[a])))
#         passer(questions())
#     elif a.__contains__('Do you'):
#         if 'Do' in a:
#             a=re.sub('Do',"Yes",a)
#         if 'you' in a:
#             a = re.sub('you', "I", a)
#         if 'my' in a:
#             a=re.sub('my','your',a)
#         print(bot.format(a+"."))
#         passer(questions())
#
#     else:
#         print(bot.format(random.choice(myDictionary['Default'])))
#         passer(questions())
#
#
# def passer(a):
#     if a.endswith('?') or a.endswith('!') or a.endswith('.'):
#         b=a[len(a)-1]
#         a=a[0:a.index(b)]
#         a.lower()
#     response(a)
# passer(questions())
# from datetime import datetime
#
# releaseDate="2020-08-15"
# releaseDate=datetime.strptime(releaseDate,"%Y-%m-%d")
# releaseDate=releaseDate.replace(month=datetime.now().month)
# print(releaseDate)
# if datetime.now() > releaseDate:
#     min=datetime.now().strftime("%Y-%m-%d")
#
# elif datetime.now() <= releaseDate:
#     min=releaseDate.strftime("%Y-%m-%d")
#
# print(min)

# a=int(input("Enter a number"))
# if a%100 !=0:
#     print(a-(a%100))

#
# import re
#
# a="Bot: {0}"
# statement="I am a good boy!!"
#
# if "I" in statement:
#     statement=re.sub("I","Sagar",statement)
#
# if "am" in statement:
#     statement=re.sub("am","is",statement)
#
# print(a.format(statement))


# import random
# result='Winner for giveaway is {}.'
# rp={
#     "regular":['1','2','3','4','5'],
#     "supporter":['6','7','8','9']
# }
#
#
# b=random.randint(1,100)
# if b>5 and b<=20:
#     choices='supporter'
# else:
#     choices='regular'
#
#
# print(result.format(random.choice(rp[choices])))
#
#
# from datetime import datetime
#
# a="1999-06-01"
# b=datetime.now()
# a=datetime.strptime(a,"%Y-%m-%d")
#
# c=int((((b-a).days-1)/365))
# print(f'{c} years')

# import random
#
# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[]
#
# while len(list2) != len(list1):
#     b = random.randint(0, len(list1)-1)
#     if list1[b] not in list2:
#         list2.append(list1[b])
#
# list3=list(zip(list2,list1))
# print(list3)
# for i in range(0,len(list3)):
#     for j in range(0,len(list3[i])):
#         for k in range(1,11):
#             print(f'{list3[i][j]}*{k}={list3[i][j]*k}')
#         print()
#     print()


# searchLetter='sagar'
# user="user: {}"
#
#
# import  re
# pattern='\d'
#
# def askUser():
#     userQuestion=input("Enter your sentence: ")
#     return userQuestion
#
# def searchEngine(a):
#     a=a.split(' ')
#     count=0
#     for i in range(0,len(a)):
#         if a[i] == searchLetter.lower():
#             count+=1
#     print(f'Sagar is repeated for {count} number(s) of times in sentence.')
# def response(sentence):
#     sentence=sentence.lower()
#     if re.search(pattern,sentence) == True:
#         print('PLease donot provide integers.')
#     elif sentence.endswith('?'):
#         sentence=sentence[0:len(sentence)-1]
#         searchEngine(sentence)
#     else:
#         searchEngine(sentence)
#
#
#
# response(askUser())

#
# a=['Sagar','Samir','Adsa']
# a=sorted(a,reverse=False)
# print(a)
#
from datetime import datetime, timedelta

# nextMonth=f'{datetime.now().year}-{datetime.now().month+1}-01'
# for i in range(1,13):
#     if i+1<=12:
#         nextMonth=f'{datetime.now().year}-{i+1}-01'
#         nextMonth=datetime.strptime(nextMonth,"%Y-%m-%d")
#         lastDate=(nextMonth+timedelta(-1)).strftime("%B-%d")
#         print(lastDate)
#     else:
#         nextMonth = f'{datetime.now().year+1}-01-01'
#         nextMonth = datetime.strptime(nextMonth, "%Y-%m-%d")
#         lastDate = (nextMonth + timedelta(-1)).strftime("%B-%d")
#         print(lastDate)

# def parsing(date):
#     newDate = datetime.strptime(date, '%Y-%m-%d')
#     end = (newDate + timedelta(-1)).strftime('%B-%d')
#     print(end)
#
# userDate='2020-12-12'
# userDate=datetime.strptime(userDate,'%Y-%m-%d')
# if userDate.month <12:
#     newDate=f'{datetime.now().year}-{datetime.now().month+1}-01'
#     parsing(newDate)
# else:
#     newDate = f'{datetime.now().year+1}-01-01'
#     parsing(newDate)

# a="2020-08-01"
# b="2020-09-01"
# a=datetime.strptime(a,'%Y-%m-%d')
# b=datetime.strptime(b,'%Y-%m-%d')
#
# print(f'{(b-a).days} Days')
#
# import re
# a='sagar1a1113'
# if re.findall('\d',a):
#     a=re.sub('\d','',a)
# print(a)

# a='1:00 p.m.'
# if 'p.m.' in a:
#     a=a.replace('p.m.','PM')
# a=datetime.strptime(a,'%I:%M %p')
# a=a.strftime('%H:%M %p')
# print(a)

# for i in range(1,8):
#     i=str(i)
#     a=datetime.strptime(i,'%d')
#     a=a.strftime('%A')
#     print(a)
# import re
# def getName():
#     name=input("Enter your name: ")
#     if re.search('\d',name):
#         print("Dont use numeric value!")
#         getName()
#     name=name.upper()
#     return name
#
#
# def getValue(value):
#     for i in range(len(value),0,-1):
#         for j in range(0,i):
#             print(value[j],end=' ')
#         print()
#     getValue(getName())
#
#
# getValue(getName())

# a='3:5 a.m.'
# if 'p.m.' in a:
#     a=a.replace('p.m.','PM')
# elif 'a.m.' in a:
#     a=a.replace('a.m.','AM')
# a=(datetime.strptime(a,'%I:%M %p')).strftime('%H:%M %p')
#
#
# b='09:00 AM'
# if b>a:
#     print(b)

rewards = {
    '1': '10 Silver Fragments',
    '2': 'Classic Scrap Coupon',
    '3': 'Supply Scrap Coupon',
    '4': '50 silver Fragments',
    '5': 'White Hitman Set',
    '6': 'Roary Dacia',
    '7': 'Common Tshirt',
    '8': 'Common Sweater',
    '9': '100 silver Fragments',
    '10': 'Fire Dance Emote'
}

# import random
# count=0
# rewardAt=str(random.randint(15,16))
# user='You got {}'
# def noWinner():
#     global count
#     if count >= 5:
#         winner()
#     else:
#         noluck=str(random.randint(1,10))
#         count+=1
#         print(user.format(rewards[noluck]))
#         userChoice = input('Press Y to continue...')
#         if userChoice.lower() == 'y':
#             noWinner()
#         else:
#             pass
#
# def winner():
#     global count
#     luck = str(random.randint(15,16))
#     if luck == rewardAt:
#         print(user.format('Glacier M416'))
#         count=0
#         userChoice = input('Press Y to continue...')
#         if userChoice.lower() == 'y':
#             noWinner()
#         else:
#             pass
#     else:
#         count+=1
#         print(user.format('150 silver fragments'))
#         userChoice=input('Press Y to continue...')
#         if userChoice.lower() == 'y':
#             noWinner()
#         else:
#             pass
#
# noWinner()


# import re
#
# text='There is a cow in the garden.'
# text2=text.split('c')
# print(' blablabla '.join(text2))
# print(text)
# print(len(text))
# pattern='  '
# if re.search(pattern,text):
#     text=re.sub(pattern,' ',text)
# print(text)
# print(len(text))
#

# list1=['Title1','Title2','Title3','Title4','Title5']
# list2=[['English','Maths','Social'],['Alchemy','Sociology','Geography'],['Computer'],['Science','Humanity'],['Business Study','Account']]
#
# myList=zip(list1,list2)
# my_structure=""
# for x,y in myList:
#     my_structure+='\n\n'+''.join(x)+'\n\n'+'\n'.join([text.strip() for text in y if text.strip() != ""])
#     my_structure+='\n\n-----------'
# print(my_structure)

# import random
# list1=['Asia','Europe','Africa','North America']
# list2=[['Nepal','China','Japan','Korea'],['Germany','Spain','Italy','France'],['Senegal','Nigeria','Lebanon','Guinea'],['USA','Canada','Mexico','Panama']]
#
# continents=dict(zip(list1,list2))
# pickup1=[]
# pickup2=[]
#
#
# for i in continents.keys():
#     pickup3=[]
#     pickup1.append(i)
#     for j in range(0,2):
#         winner=random.choice(continents[i])
#         if winner not in pickup3:
#             pickup3.append(winner)
#     pickup2.append(pickup3)
#
#
# winners=dict(zip(pickup1,pickup2))
# print(winners)
#
# import re
# pattern=['/','-','^','.']
# print(len(pattern))
# sentence="Hello/ I am Sagar."
# for i in pattern:
#
#     if re.search(i,sentence):
#         print(True)
#         sentence=re.sub(i,'',sentence)
#
# print(len(sentence))
# import random
# continent=['Asia','Europe','North America']
# countries=[['Nepal','Korea','Japan','Australia'],['Germany','Switzerland','Norway','Denmark'],['USA','Canada']]
#
# merge=dict(zip(continent,countries))
#
# winners=[]
# for i in merge.keys():
#     choice=[]
#     if i == 'North America':
#         randoms = random.choice(merge[i])
#         if randoms not in choice:
#             choice.append(randoms)
#     else:
#         while len(choice) != 2:
#             randoms=random.choice(merge[i])
#             if randoms not in choice:
#                 choice.append(randoms)
#     winners.append(choice)
#
# print(dict(zip(continent,winners)))
#
#

# import re
# var = '2'
# if re.search('\d\d',var):
#     b=re.search('\d\d',var)
#     print(b)
# elif re.search('\d',var):
#     b=re.search('\d',var)
#     print(b)
#
# myTime='2:40 p.m.'
# if 'p.m.' in myTime:
#     myTime=myTime.replace('p.m.','PM')
# elif 'a.m.' in myTime:
#     myTime=myTime.replace('a.m.','AM')
#
# myTime=(datetime.strptime(myTime,'%I:%M %p')).strftime('%H:%M %p')
#
# if myTime > datetime.now().strftime('%H:%M %p'):
#     print(myTime)
# else:
#     print(datetime.now().strftime('%H:%M %p'))
# import random
# rewards={}
# epic=[]
# legendary=[]
# mythic=[]
# common=[]
# for i in range(1,31):
#     count=0
#     for j in range(1,i+1):
#         if i%j == 0:
#             count+=1
#     if count == 2:
#         epic.append(i)
#     else:
#         common.append(i)
# while len(legendary)!=4:
#     b=random.choice(epic)
#     if b not in legendary:
#         legendary.append(b)
#         epic.remove(b)
#
# while len(mythic)!=2:
#     b=random.choice(epic)
#     if b not in mythic:
#         mythic.append(b)
#         epic.remove(b)
# while len(epic) <8:
#     b=random.choice(common)
#     if b not in epic:
#         epic.append(b)
#         common.remove(b)
#
# mythicItem=['Inferno rider helmet','Mummy Set']
# legendaryItem=['Bape Xsuit','Hell fire AKM','Fools M416','Unicorn M762']
# epicItem=['Glacier M416','Blood Sweater','Nurse Dress','Helmet','Buggy','Dacia','Suit','Ragnarok Suit']
# commonItem=['Tshirt','Pant','Sticker','Spectacle','Belt','Shoes']
# randoms=['10 silver fragments','20 silver fragments','50 silver fragments','Sticker']
# while len(commonItem) != len(common):
#     commonItem.append(random.choice(randoms))
#
# numberContainer=[]
# itemContainer=[]
#
# numberContainer.extend(mythic)
# numberContainer.extend(legendary)
# numberContainer.extend(epic)
# numberContainer.extend(common)
#
# itemContainer.extend(mythicItem)
# itemContainer.extend(legendaryItem)
# itemContainer.extend(epicItem)
# itemContainer.extend(commonItem)
#
# rewards=dict(zip(numberContainer,itemContainer))
# viewer=""
# for i in rewards.values():
#     viewer+=i+','
# print(viewer[0:len(viewer)-1])
# user='You got {}'
#
# def itemGained():
#     number=random.randint(1,30)
#     print(user.format(rewards[number]))
#     print(number)
#     choice=input('Press Y to continue..')
#     if choice.lower() == 'y':
#         itemGained()
# choice=input('Press Y to open crate..')
# if choice.lower() == 'y':
#     itemGained()
#
# import string
# import random
# participants=list(string.ascii_uppercase)
# roundOf32=[]
# roundOf16=[]
# roundOf8=[]
# roundOf4=[]
# roundOf2=[]
# matchWinners=[]
# winner='Winner is {}'
# i=0
# while len(participants) != 32:
#     participants.append(participants[i]+str(i+1))
#     i+=1
#
#
# def matchMaker(myList,type):
#
#     a = random.choice(myList)
#     b = random.choice(myList)
#     if a != b:
#         if type == 32:
#             roundOf32.append([a, b])
#             participants.remove(a)
#             participants.remove(b)
#         elif type == 16:
#             roundOf16.append([a, b])
#             matchWinners.remove(a)
#             matchWinners.remove(b)
#         elif type == 8:
#             roundOf8.append([a, b])
#             matchWinners.remove(a)
#             matchWinners.remove(b)
#         elif type == 4:
#             roundOf4.append([a, b])
#             matchWinners.remove(a)
#             matchWinners.remove(b)
#
# def pickWinner(matches):
#
#     global  matchWinners
#     matchWinners=[]
#     for i in range(0,len(matches)):
#         matchWinners.append(random.choice(matches[i]))
# print(participants)
# while len(roundOf32) != 16:
#     matchMaker(participants,32)
# if len(roundOf32) == 16:
#     pickWinner(roundOf32)
#
# print(matchWinners)
#
# while len(roundOf16) != 8:
#     matchMaker(matchWinners,16)
#
# if len(roundOf16) == 8:
#
#     pickWinner(roundOf16)
# print(matchWinners)
# while len(roundOf8) != 4:
#     matchMaker(matchWinners,8)
#
# if len(roundOf8) == 4:
#
#     pickWinner(roundOf8)
# print(matchWinners)
# while len(roundOf4) != 2:
#     matchMaker(matchWinners,4)
#
# if len(roundOf4) == 2:
#
#     pickWinner(roundOf4)
# print(matchWinners)
# print(winner.format(random.choice(matchWinners)))


import re

# text='£1500 a year'
# currency = re.findall(r'[\£]\b\d+\b', (text.replace(',','')))
# if len(currency) >= 1:
#     currency[0]=currency[0].replace('£','')
#
# print(currency)
#
#
# a='My income is $20000, $30000'
# ab = re.findall(r'[\$]\d+',(a.replace(',','')))
# for i in ab:
#     if '$' in i:
#         i=i.replace('$','')
#         print(i)

import re
# forFilter = {
#     'Ashish': 'Earns $4000 per month',
#     'Sagar': 'Earns $5000 per month',
#     'Abhishek': 'Earns $3500,$4000per month'
# }
#
#
#
# for x,y in forFilter.items():
#     y=y.strip()
#     b=re.findall(r'[\$]\d+',(y.replace(',',''))) or re.findall(r'[\$] \d+',(y.replace(',','')))
#     for i in range(0,len(b)):
#         if '$' in b[i]:
#             b[i]=b[i].replace('$','')
#             b[i]=int(b[i])
#     forFilter[x]= sum(b)
# print(forFilter)

# user='User:{}'
# inputVal=input('Write message:')
# b='fuck'
# if re.findall(b,inputVal.lower()):
#
#     repeatCount=re.findall(b,inputVal.lower())
#     if len(repeatCount) >=4:
#         print(f'Messages deleted due to {len(repeatCount)} times repetition of inappropriate word!!')
#     else:
#         print(user.format(inputVal))


# val='Sagar Sagarsagar'
# print(val.lower().count('sagar'))

# import re
# details='1.Abhishek:Rs 50000,2.Sagar:Rs 120000,3.Ashish:Rs 80000'
# details=details.replace(',','') and details.replace('Rs','$')
#
# list1=re.findall(r'[\.][A-Z][a-z]+',details) or re.findall(r'[\.] [A-Z][a-z]+',details)
# list2=re.findall(r'[\$] \d+',details) or re.findall(r'[\$]\d+',details)
# for i in range(0,len(list1)):
#     list1[i]=list1[i].replace('.','')
# for i in range(0, len(list2)):
#     list2[i]=list2[i].replace('$','')
#     list2[i]=int(list2[i])
#
# #mappings2=[(x,y) for x in list1 for y in list2 if list1.index(x) == list2.index(y)]
#
# mappings=dict(zip(list1,list2))
# print(mappings)
# #print(dict(mappings2))
# print(f'Overall money: Rs {sum(list2)}')
#
# import string
# import random
#
# a=string.ascii_uppercase
# a=''.join(a)
# b=string.ascii_lowercase
# b=''.join(b)
# c="0123456789"
# overall=(a+b+c+'$').strip()
#
# listOfPass=[]
# totalPassword=int(input('Enter total number of required passwords: '))
# winner=[]
# repeated=[]
# for i in range(0,totalPassword):
#     randomPass = ""
#     while(len(randomPass) != 6):
#         randomIndex=random.randint(0,len(overall)-1)
#         randomPass+=overall[randomIndex]
#
#     if '$' in randomPass:
#         if len(winner) == 0:
#             randomPass = randomPass.replace('$', '')
#             randomPass += "$" + str(random.randint(1,100))
#             winner.append(randomPass)
#     if randomPass in listOfPass:
#         repeated.append(randomPass)
#     listOfPass.append(randomPass)
# print(listOfPass)
# if len(winner) == 0:
#     print('No one was selected!!')
# else:
#     print(winner[0].split('$'))
#
# print(repeated)

# import random
# print("********Sagar's Giveaway********")
# regular=['Sagar','Abhishek','Ashish','Basanta','Krishna','Ankit','Sakriya','Ashwan','Bishesh','Nima']
# supporter=['Samir','Kritika','Sujan','Suman','Manav','Saina','Salina']
# remain=[]
# totalWinners={}
# print(f'Total Candidates: {len(regular)+len(supporter)}')
# estimatedWinnersCount=int(input("Enter total number of winners: "))
#
# def checkWinner(person,list1):
#     # if person in totalWinners.keys():
#     #     return False
#     # else:
#     #     totalWinners[person]=random.randint(10,10000)
#     money=random.randint(0,10000)
#     print(f'{person}:{money}')
#     count=1
#     if money >= 5000:
#         while count !=3:
#
#
#             money=random.randint(0,10000)
#             print(f'{person}:{money}')
#             if money >= 2000:
#                 count+=1
#             else:
#                 break
#     totalWinners[person]=money
#     list1.remove(person)
#
#
# def getWinner(choice):
#     if choice < 20:
#         if len(supporter)>0:
#             winner=random.choice(supporter)
#             checkWinner(winner,supporter)
#         else:
#             winner=random.choice(regular)
#             checkWinner(winner,regular)
#     else:
#         if len(regular)>0:
#             winner=random.choice(regular)
#             checkWinner(winner,regular)
#         else:
#             winner=random.choice(supporter)
#             checkWinner(winner,supporter)
#
# while len(totalWinners) != estimatedWinnersCount:
#     if len(regular)+len(supporter) == 0:
#         print('There is no person to receive this giveaway!!')
#         break
#     else:
#         winnerChoice=random.randint(1,100)
#         winner=getWinner(winnerChoice)
#
# print(totalWinners)
# remain.extend(regular)
# remain.extend(supporter)
# total=0
# for j in totalWinners.values():
#     total+=j
# print(f'Dont lose hope: {remain}')
# print(f'Total Investment: ${total}')
#
# import random
# value=int(input("Enter how many phone numbers required: "))
# codec=int(input('Enter codec: '))
# phoneNumbers=[]
# while len(phoneNumbers) != value:
#     start=str(codec)
#     for i in range(1,8):
#         start+=str(random.randint(0,9))
#     if start not in phoneNumbers:
#         phoneNumbers.append(start)
#
# print(phoneNumbers)

#
# fullTimeAndDate='Tuesday. April 2020 2:45 p.m.'
# if 'p.m.' in fullTimeAndDate:
#     fullTimeAndDate=fullTimeAndDate.replace('p.m.','PM')
# if 'a.m.' in fullTimeAndDate:
#     fullTimeAndDate=fullTimeAndDate.replace('a.m.','AM')
#
# fullTimeAndDate=(datetime.strptime(fullTimeAndDate,'%A. %B %Y %I:%M %p')).strftime('%Y-%m-%d %H:%M %p')
# print(fullTimeAndDate)

#
# list1=[1,0,1]
# list2=[]
# for i in range(len(list1)-1,-1,-1):
#     list2.append(list1[i])
#
# count=0
# for i in range(0,len(list1)):
#     if list1[i] == list2[i]:
#         count+=1
#     else:
#         print('Not a palindrome')
#         break
# if count == len(list1):
#     print('Palindrome')

# price=232
# qty=int(input("Enter the quantity: "))
# bill=price*qty
# print(bill)
# if bill % 5 != 0:
#     bill=(bill-(bill%5))+5
# print(bill)

#
# import random,re,string,sys
# class Person:
#
#     def __init__(self,fullname,age,email,phoneNumber):
#         self.fullName=fullname
#         self.age=age
#         self.email=email
#         self.phoneNumber=phoneNumber
#
#     def habit(self):
#         self.myhabits=input("Enter your habits: ")
#         self.aim=input("Entter your aim: ")
#         self.hobby=input("Enter your hobby: ")
#
#     def printing(self):
#         print(f'I am {self.fullName}. \nI am {self.age} years old. \nMy email is {self.email}. \nMy phone number is {self.phoneNumber}.')
#         print(f'My hobby is {self.myhabits.strip()}.')
#         print(f'My aim is {self.aim.strip()}.')
#         print(f'My hobby is {self.hobby.strip()}.')
#
#
# class University(Person):
#     universityName='Coventry University'
#     def __init__(self,fullname,age,email,phoneNumber):
#         super().__init__(fullname,age,email,phoneNumber)
#
#         self.enterCode=self.getEnterCode()
#         self.printData()
#     def getEnterCode(self):
#         upperCase=string.ascii_uppercase
#         lowerCase=string.ascii_lowercase
#         jumble=''.join(upperCase)+''.join(lowerCase)+'0123456789'
#         enterCode=''
#         while len(enterCode) != 6:
#             randomIndex=random.randint(0,len(jumble)-1)
#             enterCode+=jumble[randomIndex]
#         return enterCode
#     def printData(self):
#         print(f'University: {University.universityName}')
#         print(f'Entering code for {self.fullName} is: {self.enterCode}')
#         team=self.getTeam()
#         if team:
#             print(f'You are added to {team} team.')
#         else:
#             print('Every teams are packed right now!!')
#         b='y'
#         if b:
#             flag=0
#             codeCheck = input('Enter your code: ')
#             while flag != 1:
#
#
#                 if codeCheck == self.enterCode:
#                     flag=1
#                     print('Succesfully terminated!!')
#                     sys.exit()
#                 else:
#                     codeCheck=input('ReEnter your code: ')
#                     flag=0
#     def getTeam(self):
#         team = ''
#         keyContainer=[]
#         teams={
#             'Hydra':[1,2,3,4],
#             'Unicorn':[5,6,7,8],
#             'Flower':[9,1,2]
#         }
#         for x in teams.keys():
#             keyContainer.append(x)
#
#         flag = 0
#
#         while flag != 1:
#             if len(keyContainer)<=0:
#                 break
#             else:
#                 getData = random.choice(keyContainer)
#                 if len(teams[getData]) >=4:
#                     flag=0
#                     keyContainer.remove(getData)
#                 else:
#                     team=getData
#                     teams[getData].append(self.fullName)
#                     flag=1
#         return team

# def validation(items):
#     if re.search(r'[a-z][a-z]+',items['phoneNumber']):
#         return f'{items["name"]}: Invalid phone number!!'
#     elif re.search(r'[a-z][a-z]+',str(items['age'])):
#         return f'{items["name"]}: Phone number should be in numeric field!!'
#     elif re.search(r'@[a-z]+.com',items['email'].lower()) == False:
#         return f'{items["name"]}: Email should contain @.'
#     else:
#         return True



#uni=University("sagar",20,'sagarcrcoc@gmail.com','9803609163')


# objectsContainer=[]
# try:
#     totalObjects=int(input('Required amount of staffs is: '))
#     while len(objectsContainer) != totalObjects:
#         name = input('Enter your full name: ')
#         age = input('Enter your age: ')
#         email = input('Enter your email address: ')
#         phoneNumber = input('Enter your phone number: ')
#         items = {
#             'age': age,
#             'email': email,
#             'phoneNumber': phoneNumber,
#             'name': name
#         }
#         check = validation(items)
#         if check == True:
#             uobj = University(name, age, email, phoneNumber)
#             objectsContainer.append(uobj)
#             print('Data added')
#         else:
#             print(check)
#             print('Re-enter data')
#
#     for i in objectsContainer:
#         i.printData()
# except Exception as e:
#     print(f'Exception raised: {e}')


# import random
# class giveaway:
#     title='ABC Giveaway'
#     winnerContainer=[]
#     def __init__(self):
#         participants=self.findParticipants()
#         giveawayItems=self.assignItems()
#         winners=self.getWinner(participants,giveawayItems)
#         print(winners)
#     def findParticipants(self):
#
#         regular=[]
#         supporter=[]
#         participants={
#             'sagar12345':20,
#             'samir':10,
#             'kritika':15,
#             'absek':12,
#             'asis':30,
#             'ankit':40,
#             'sakriya':23,
#             'bises':12,
#             'krishna':10,
#             'basanta':19
#         }
#         for x,y in participants.items():
#             if participants[x] > 20:
#                 regular.append(x)
#             elif participants[x] < 20:
#                 supporter.append(x)
#         records={
#             'regular':regular,
#             'supporter':supporter
#         }
#         return records
#     def assignItems(self):
#         giveAwayItems={
#             'Tshirt':2,
#             'Pant':3,
#             'Shoes':2
#         }
#         return giveAwayItems
#     def getWinner(self,participants,items):
#         data=max(items.values())
#
#         while len(giveaway.winnerContainer)!=data:
#             estimation = random.randint(1, 100)
#             if estimation < 40:
#                 if len(participants['supporter']) > 0:
#
#                     winner=random.choice(participants['supporter'])
#                     giveaway.winnerContainer.append(winner)
#                     participants['supporter'].remove(winner)
#                 elif len(participants['regular']) > 0:
#                     winner = random.choice(participants['regular'])
#                     giveaway.winnerContainer.append(winner)
#                     participants['regular'].remove(winner)
#             elif estimation > 60:
#                 if len(participants['regular']) > 0:
#
#                     winner = random.choice(participants['regular'])
#                     giveaway.winnerContainer.append(winner)
#                     participants['regular'].remove(winner)
#                 elif len(participants['supporter']) > 0:
#                     winner = random.choice(participants['supporter'])
#                     giveaway.winnerContainer.append(winner)
#                     participants['supporter'].remove(winner)
#         prizeDistribution=self.distribute(items)
#         return prizeDistribution
#
#     def distribute(self,items):
#         winners={}
#         for i in range(0,len(giveaway.winnerContainer)):
#             if sum(items.values()) > 0:
#                 winners[giveaway.winnerContainer[i]]=[]
#                 for x,y in items.items():
#                     if items[x] > 0:
#                         winners[giveaway.winnerContainer[i]].append((x,1))
#                         items[x]=y-1
#         return winners
#
#
# for i in range(0,2):
#     gc=giveaway()
#
#

#
#
# import re
# class records:
#     office='Office of Data and Information'
#     bank=59999
#     def __init__(self):
#         employees=self.getEmployees()
#
#     def getEmployees(self):
#         employeeCatlog={
#             'Sagar':'payment required Rs 30000',
#             'Samir':'payment required Rs 20000',
#             'Kritika':'payment required Rs10000'
#         }
#         keys=[]
#         payments=[]
#         keys.extend(employeeCatlog.keys())
#         payments.extend(employeeCatlog.values())
#         filterPayments=self.filterData(payments)
#         assignPrice=self.assign(filterPayments)
#         paymentCatlog={}
#         for i in range(0,len(assignPrice)):
#             paymentCatlog[keys[i]]=f'received Rs {assignPrice[i][0]}'
#             if assignPrice[i][1] == 0:
#                 employeeCatlog[keys[i]] = f'full paid'
#             else:
#                 employeeCatlog[keys[i]]=f'payment required Rs {assignPrice[i][1]}'
#         print(paymentCatlog)
#         print(employeeCatlog)
#
#     def filterData(self,payments):
#         obtainedData=[]
#         for i in payments:
#             if 'Rs' in i:
#                 data=i.replace('Rs','$').strip()
#             else:
#                 data=i.strip()
#             req=re.findall(r'[\$] \d+',data.replace(',','')) or re.findall(r'[\$]\d+',data.replace(',',''))
#             obtainedData.append(int(req[0].replace('$','')))
#         return obtainedData
#
#     def assign(self,filteredAmount):
#         totalWage=sum(filteredAmount)
#         percentDistribution=(records.bank/totalWage)*100
#         received=[]
#         for i in filteredAmount:
#             received.append([((percentDistribution/100)*i).__round__(1),(i-((percentDistribution/100)*i).__round__(1)).__round__(1)])
#
#         return received
#
# rc=records()
#


# import string,random
# dataContainer=[]
# person=['Sagar','Samir','Kritika','Absek','Asis','Abc','Xyz','ttt','yyy','adad']
# overallData=''.join(string.ascii_uppercase)+''.join(string.ascii_lowercase)+'0123456789'
# while len(dataContainer) != 5:
#     passContainer=[]
#     alphabetCount=6+len(dataContainer)
#     while len(passContainer )!= 10:
#         password=''
#         while len(password) != alphabetCount:
#             randIndex=random.randint(0,len(overallData)-1)
#             password+=overallData[randIndex]
#         passContainer.append(password)
#     dataContainer.append(passContainer)
#
#
# totalItems=[]
# dataHolder=[]
# while len(totalItems) != len(person):
#     if len(dataHolder) == len(dataContainer):
#         while(len(dataHolder)> 0):
#             dataHolder.pop()
#     flag=0
#     while flag != 1:
#         index=random.randint(0,len(dataContainer)-1)
#         if index not in dataHolder:
#             flag=1
#             valuess=random.choice(dataContainer[index])
#             totalItems.append(valuess)
#             dataHolder.append(index)
#             dataContainer[index].remove(valuess)
#
#
#         else:
#             flag=0
#
# values=dict(zip(person,totalItems))
# print(values)
# print(len(values))

#
#
# checkDict=[
#     {
#     'name':'Sagar',
#     'salary':1000000,
#     'age':20,
#     'hobby':['football','coding','FPS games']
#     },
#     {
#     'name':'Abhishek',
#     'salary':200000,
#     'Age':21,
#     'hobby':['PC games','Gym','bike','football']
#     }
# ]
#
#
# hobby=[]
# for i in checkDict:
#     description=''
#     myDetails=[]
#     for x,y in i.items():
#         myDetails.append(y)
#         if x == 'hobby':
#             hobby.extend(y)
#     description+=f'Hi, My name is {myDetails[0]}. \nI earn Rs {myDetails[1]} per month. \nI am {myDetails[2]} years old. \nMy hobby is {",".join(myDetails[3])}'
#
#
# hobby=list(map(lambda x: x.lower(),hobby))
# myValues={}
# # data1=[{hobby[x]:hobby.count(hobby[x])} for x in range(0,len(hobby)) if hobby.count(hobby[x])>1]
# #
# # for i in data1:
# #     for x in i.keys():
# #         if data1.count(i) > 1:
# #             data1.remove(i)
#
# for i in hobby:
#
#     myValues[i]=hobby.count(i)
#
# repeated=max(myValues.values())
# for x,y in myValues.items():
#     if y == repeated:
#         print(f'{x} : {y}')


#
# totalData=[
#     {
#
#     'first_name':'Sagar',
#     'last_name':'Mishra',
#     },
#     {
#         'first_name':'Samir',
#         'last_name':'Mishra'
#     },
#     {
#         'first_name':'Kritika',
#         'last_name':'Mishra'
#     }
# ]

#
# def letsRocknRoll():
#     user=input('Enter your name: ')
#     for i in range(0,len(user)):
#         for j in range(0,i+1):
#             print(user[j],end=' ')
#         print()
#     return lambda x: x*len(user)
#
# data=letsRocknRoll()
# print(data(2))

# import re
# a='Sagar earns just $20000,$50000 a month.'
#
# earnings=re.findall(r'[\$]\d+',a)
# earnings.extend(re.findall(r'[\$] \d+',a))
# print(earnings)
# data=','.join(earnings)
# print(data)
# earnings=list(map(lambda x:int(x.replace('$','')),earnings))
# data2='$'+str(sum(earnings))
# a=a.replace(data,data2)
# print(a)

# class fileRead:
#     company='File Association'
#     def __init__(self,fileName,extension,mode):
#         self.fileName=fileName
#         self.extension=extension
#         self.mode=mode
#         self.workWithFile()
#
#     def workWithFile(self):
#         try:
#
#             fileData=open(self.fileName+'.'+self.extension,mode=self.mode)
#             if self.mode == 'r':
#                 f=fileData.readlines()
#                 for i in f:
#                     print(i)
#             elif self.mode == 'a+':
#                 iteration=int(input('Enter the iteration count: '))
#                 for i in range(0,iteration):
#                     inputData=input(f'Enter what you want to add to the file in line {i+1}: ')
#                     fileData.write('\n'+inputData)
#             elif self.mode == 'w+':
#                 iteration = int(input('Enter the iteration count: '))
#                 for i in range(0, iteration):
#                     inputData = input(f'Enter what you want to add to the file in line {i + 1}: ')
#                     fileData.write('\n' + inputData)
#             fileData.close()
#         except Exception as e:
#             print(f'Be sure you have provided correct file name and extension. {e}')
#
#
#
# fileName=input('Enter the name of the file: ')
# fileExtension=input('Enter the extension of the file: ')
# mode=input('Enter the mode for file handling: ')
# fr=fileRead(fileName,fileExtension,mode)

# import re
# twoTimes={
#     'Sagar':'Earns $4 per month',
#     'Ashish':'Earns $3500,$4500 per month',
#     'Abhishek':'Earns $2500,$6500,$ 12000 per month'
# }
#
# for x,y in twoTimes.items():
#     money=re.findall(r'[\$]\d+',y)
#     money.extend(re.findall(r'[\$] \d+',y))
#     data=','.join(money)
#
#     filters=list(map(lambda x:int(x.replace('$','')),money))
#
#     twoTimes[x]=y.replace(data,f'${sum(filters)}')
#
# print(twoTimes)

# import random
# gift={
#     'Glacier':2,
#     'AKM':2,
#     'UMP45':1
# }
# winners=['Sagar','Ashish']
# distribution={}
# while len(distribution)!=len(winners):
#     for i in winners:
#         randomPerson=random.choice(winners)
#
#         if randomPerson not in distribution.keys():
#             if sum(gift.values())>0:
#                 distribution[randomPerson]=[]
#                 for x,y in gift.items():
#                     if y>0:
#                         distribution[randomPerson].append(x)
#                         gift[x]=y-1
#
# description=''
# for x,y in distribution.items():
#     description+=f'{x} got {",".join(y)}\n'
#
# print(description)


# import re
# givenData=['sagar20','samir105','kritika19','dan1']
# filteredData=[]
# for i in givenData:
#     #filteredData.extend(re.findall(r'\d+',i))
#     filteredData.append(i[len(i)-1])
# filteredData=list(map(lambda x:int(x),filteredData))
# print(filteredData)

# import re
# obtainedData=['1#dfsd132dfs2312','45adas1213#121']
# dataHolder=[]
# originalData=[]
# for i in obtainedData:
#     dataHolder.extend(re.findall(r'\d+',i))
#     originalData.append(''.join(dataHolder))
#     dataHolder=[]
# originalData=list(map(lambda x:int(x),originalData))
# print(originalData)

# individualSatisfaction={}
# userSatisfaction={
#     'Sagar':[3,4,5,1,0,0,0,5],
#     'Samir':[1,2,3,4,5],
#     'Kritika':[5,0,0,0]
# }
# for x,y in userSatisfaction.items():
#     dummyList=[]
#     for i in y:
#         dummyList.append(100-(i*20))
#
#     avg=sum(dummyList)/len(dummyList)
#     individualSatisfaction[x]=round(avg,2)
#
# print(individualSatisfaction)
# print(f'Total satisfaction is {round(sum(individualSatisfaction.values())/len(individualSatisfaction),2)}%')

# import string,random
# mainContainer=[]
# overall=''.join(string.ascii_uppercase)+''.join(string.ascii_lowercase)+'0123456789'
# while len(mainContainer)!=10:
#     code=''
#     while len(code) !=6:
#         randIndex=random.randint(0,len(overall)-1)
#         code+=overall[randIndex]
#     if code not in mainContainer:
#         mainContainer.append(code)
#     else:
#         print('Found')
# print(mainContainer)
# subjects=['English','Nepali','Maths','Social','Science','Opt Maths','EPH','Computer']
# highestHolder=['','','','','','','','']
# highestMarks=[0,0,0,0,0,0,0,0]
# percentage={}
# userObtainedMarks={
#     'Sagar':[80,50,90,50,75,95,70,90],
#     'Nadir':[100,40,40,40,70,30,75,80],
#     'Anjum':[65,45,65,45,70,70,70,90]
# }
# for x,y in userObtainedMarks.items():
#     obtainedPercentage=round((sum(y)/8),2)
#     percentage[x]=obtainedPercentage
#     for i in range(0,len(y)):
#         if y[i] > highestMarks[i]:
#             highestMarks[i]=y[i]
#
#             highestHolder[i]=x
#         elif y[i] == highestMarks[i]:
#             highestHolder[i]=highestHolder[i]+','+x
#
# val1=list(zip(highestHolder,highestMarks))
# val2=dict(zip(subjects,val1))
# print(val2)

#
# tracking={}
# firstThree={}
# persons={
#     'Sagar':'Icecream,Momo,Coke,Pizza,Momo,Momo,Pizza,Momo,Chowmin,Grilled Chicken',
#     'Samir':'Momo,Coke,Burger,Sandwich,Burger,Chicken Popcorn',
#     'Kritika':'Cashew,Spinach,Momo,Coke,Momo,Momo,Pizza,Pizza,Chicken Roast'
# }
#
# for x,y in persons.items():
#     userChoices=y.split(',')
#     if x not in tracking.keys():
#         tracking[x]={}
#         for i in userChoices:
#             if i not in tracking[x].keys():
#                 tracking[x][i]=userChoices.count(i)
#
# for x,y in tracking.items():
#     dummyList=list(y.values())
#     dummyList.sort(key=lambda x:x,reverse=True)
#     dummyList=dummyList[0:3]
#     firstThree[x]=[]
#     i=0
#     flag=0
#     while len(firstThree[x])!=2 and flag == 0:
#         for j,k in y.items():
#             if k == dummyList[i]:
#                 firstThree[x].append(j)
#         if len(firstThree[x])>=2:
#             flag=1
#         else:
#             i+=1
# print(firstThree)
# import time,sys
#
#
#
#
# def userChoice():
#     userInput=int(input("Enter the number from 1-12: "))
#     return userInput
#
# def continueYeah():
#     userGuide=input('Press Y to continue:')
#     if userGuide.lower() == 'y':
#         convertData(userChoice())
#     else:
#         sys.exit()
#
# def convertData(userValue):
#     if userValue > 12 or userValue<0:
#         print(f'Please provide valid value!!')
#         userValue=12
#     parsedData=(datetime.strptime(str(userValue),'%m')).strftime('%B')
#     print(parsedData)
#     print('Sleeping for 3 seconds...')
#     time.sleep(3)
#     continueYeah()
#
# convertData(userChoice())

# import re
# given='sadadas4d5,sdas2sdasd4'
# given=given.split(',')
# valuess=[]
# for i in given:
#     dataLocator=re.findall(r'\d+',i)
#     dataLocator=''.join(dataLocator)
#     valuess.append(int(dataLocator))
# print(valuess)

# import time,re
#
# def getData():
#     myData={
#         'Sagar':'need to pay $7000,$ 6000 in 2020-11-05',
#         'Ashish':'need to pay $5500 in 2020-11-20',
#         'Abhishek':'need to pay $6000 in 2020-11-25'
#     }
#     return myData
#
# def giveDetails(data):
#     print('Data filtered...')
#     time.sleep(1)
#     print('Ready to show...')
#     time.sleep(1)
#     description=''
#     for x,y in data.items():
#         description+=f'{x} needs to be paid ${y[0]} in {y[1]} days. \n'
#     print(description)
# def filterDate(data):
#     print('Data obtained...')
#     time.sleep(1)
#     for x,y in data.items():
#         data[x]=[y[0],datetime.strptime(y[1],'%Y-%m-%d')]
#     today=datetime.now()
#     for x,y in data.items():
#         data[x]=[y[0],(y[1]-today).days+1]
#     giveDetails(data)
# def letsWork():
#     print('Compiling...')
#     time.sleep(1)
#     b=getData()
#     collectData={}
#     for x,y in b.items():
#         collectData[x]=[]
#         amount=re.findall(r'[\$]\d+',y)
#         amount.extend(re.findall(r'[\$] \d+',y))
#         collectData[x].append(sum(list(map(lambda x:int(x.replace('$','')),amount))))
#         y=y.replace(','.join(amount),'')
#         dummyDate=re.findall(r'\d+',y)
#         collectData[x].append('-'.join(dummyDate))
#
#     filterDate(collectData)
# def sleepFor(period):
#     for i in range(1,period+1):
#         print(f'Starts in {(period+1)-i} second...')
#         time.sleep(1)
#     letsWork()
# def task():
#
#     sleepFor(1)
#
# task()

# highestTracker={}
#
# doubleDict={
#     'ManU':{'Arsenal':5,'Burnley':6,'Swansea':6},
#     'Arsenal':{'ManU':6,'Liverpool':8}
# }
#
# for x,y in doubleDict.items():
#     dummyData=list(y.values())
#     dummyData.sort(key=lambda x:x,reverse=True)
#     dummyData=dummyData[0]
#     highestTracker[x]={}
#     for j,k in y.items():
#
#             if k == dummyData:
#                 if j not in highestTracker[x].keys():
#                     highestTracker[x][j]=k
#
# print(highestTracker)


# totalData=[
#     {
#         'Name':'Sagar',
#         'Age':20
#     },
#     {
#         'Name':'Abhishek',
#         'Age':21
#     },
#     {
#         'Name':'Ashish',
#         'Age':20,
#         'Bike':'Apache 160'
#     }
#
# ]
#
# description=''
# for i in totalData:
#
#     for x,y in i.items():
#
#
#         description+=f'{x}: {y} \t'
#     description+='\n'
# print(description)
# import random
# rewards=[
#     {
#         'Glacier M416':2,
#         'Hell Fire AKM':1
#     },
#     {
#         'Parahoah Set':3,
#         'Mummy Set':2
#     }
# ]
#
# applicants=['Sagar','Samir']
# winnerAward={
#     'Sagar':[],
#     'Samir':[]
# }
# for i in rewards:
#     filtered={}
#     extra={}
#
#     for x,y in i.items():
#         if y>len(applicants):
#             filtered[x]=len(applicants)
#             extra[x]=y-len(applicants)
#         elif y <= len(applicants):
#             filtered[x]=y
#     for person in applicants:
#         if sum(filtered.values()) > 0:
#
#
#                 for x,y in filtered.items():
#                     if y>0:
#                         winnerAward[person].append((x,1))
#                         filtered[x]=y-1
#     #if sum(extra.values())>0:
#         # for x,y in extra.items():
#         #     pobj=product.objects.get(id=x)
#         #      sobj=saleAnalysis.objects.get(product=pobj.id)
#         #      sobj.totalItems=int(sobj.totalItems)
#         #     pobj.quantity=int(pobj.quantity)+y
#         #     pobj.save()
# print(winnerAward)
import random
multiDict={
    'Barclays':{'Teams':['ManU','Chelsea','Liverpool','Arsenal','Wolves','Leicester City']},
    'Laliga':{'Teams':['Real Madrid','Barcelona','Sevilla','Athletico Madrid','Valencia','Alaves']}
}
matchMaking=[]
for x,y in multiDict.items():
    dummy=[]
    for i,j in y.items():
        while len(j) != 0:
            team1=random.choice(j)
            j.remove(team1)
            team2=random.choice(j)
            j.remove(team2)
            dummy.append(f'{team1} vs {team2}')
    matchMaking.extend(dummy)

print(matchMaking)


