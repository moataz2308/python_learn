thislist =["apple","banana","cherry"]
for x in thislist:
    print(x)
Dieseliste=["Apfel","Banane","Blaubeere"]
for i in range(len(Dieseliste)):
    print(Dieseliste[i])

obst=["banana","Apfel","Tooot"]
for J in obst:
    if J=="Apfel":
        continue
    print(J)

Klasse =("Ahmed","Omar","Ammar")
for p in Klasse:
    if p=="Omar":
        continue
    elif p=="Ahmed":
        break
    print("Ahmed is found")
usernames=["Moataz","Ronaldo","messi"]
passwords=["567","777","109"]
username=input("enter your username")
password=input("neter your Password")
if (username==usernames [0 ] and password==passwords[0]) :
    print("welcome Ronaldo")
else :
    print("wrong username or password")
    

        