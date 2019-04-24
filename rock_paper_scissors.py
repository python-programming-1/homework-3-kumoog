def inputUser():
    print("make a move!(R/S/P)")
    user = input(["R", "P", "S"])
    while (user != "R" and user != "P" and user != "S"):
        print ("Wrong input input again")
        user = input(["R","P","S"])
    return user
def inputCom(b):
    if(b[0]+b[1]+b[2]+b[3]+b[4] >= 3 and b[0]+b[1]+b[2]+b[3]+b[4] <= 5):
        com = "P"
    elif(b[0]+b[1]+b[2]+b[3]+b[4] >= 30 and b[0]+b[1]+b[2]+b[3]+b[4] <= 50):
        com = "R"
    elif(b[0]+b[1]+b[2]+b[3]+b[4] >= 300 and b[0]+b[1]+b[2]+b[3]+b[4] <= 500):
        com = "S"
    else:
        com = random.choice(["R", "P", "S"])
    return com
def decision(com,user):

    if (com == user):
        print("It is tie!!")
        return "T"
    elif (com == "R" and user == "P"):
        print("You win")
        return "W"
    elif (com == "R" and user == "S"):
        print("You lose")
        return "L"
    elif (com =="P" and user =="S"):
        print("You win")
        return "W"
    elif (com =="P" and user == "R"):
        print("You lose")
        return "L"
    elif (com == "S" and user == "R"):
        print("You win")
        return "W"
    elif (com == "S" and user == "P"):
        print("You lose")
        return "L"
def yesnodecision():
    print("Do you want to play again?(Y/N)")
    yesno = input(["Y","N"])
    while(yesno != "Y" and yesno != "N"):
        print("Wrong input! please input again(Y/N)")
        yesno = input(["Y","N"])
        return yesno






import random
comwin = 0
userwin =0
yesno = "Y"
i=0
a = [0,0,0,0,0]
b = [0,0,0,0,0]

while comwin + userwin !=5 and yesno != "N":
    com = inputCom(b)
    user = inputUser()
    result = decision(com, user)
    if (result == "W"):
        userwin = userwin+1
    elif (result == "L"):
        comwin = comwin +1
    while (result =="T"):
        user = inputUser()
        com = inputCom(b)
        result = decision(com, user)
        if (result == "W"):
            userwin = userwin +1
            break
        elif (result == "L"):
            comwin = comwin +1
            break
    a[i] = user
    if (a[i] == "R"):
        b[i] = 1
    elif (a[i] == "S"):
        b[i] = 10
    elif (a[i] == "P"):
        b[i] =100
    i = i+1

    if (comwin + userwin == 5):
        print("comwin:", comwin, "userwin:", userwin)
        break
    yesno = yesnodecision()
    if(yesno == "Y"):
        continue
    elif(yesno == "N"):
        print("comwin:",comwin,"userwin:",user)
        break
