import random as rd
arr=["Rock","Paper","Scissor"]
choice=1
while choice!=0:
    cmpChoice=rd.randint(1,3)
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    choice=int(input("Enter your choice:"))

    if cmpChoice==1 and choice==3 or cmpChoice==2 and choice==1 or cmpChoice==3 and choice==2:
        print("Computer wins it chosen",cmpChoice)
    elif cmpChoice==3 and choice==1 or cmpChoice==1 and choice==2 or cmpChoice==2 and choice==3:
        print("You won !!!!")
    else:
        print("Tiee !!!")