def inputUser():

    while(True):
        try:
            print("input positive number")
            user = int(input())
            if user >0:
                collatz(user)
                break
            else:
                print("This is negative number or 0!!!")
                continue


        except ValueError:
            print("input wrong number\n")

            continue



def collatz(user):
    print("current user number is ", user)
    while(user != 1):
        if(user%2 == 1):
            user = (3*user)+1
            print("now the user number is ", user)

        else:
            user =user/2
            print("now the user number is ", user)


inputUser()







