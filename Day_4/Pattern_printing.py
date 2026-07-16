#Right Angle Triangle
# rows = int(input("Enter the rows : "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    


#Pyramid
# rows= int(input("Enter the rows :"))
# for i in range (1,rows+1):
#     for k in range(rows,i,-1):
#         print(" ",end="")    
#     for j in range(1,i+1):
#         print("*",end=" ") 
#     print()  


# DIAMOND PRINTING
# row=int(input("Enter the number of rows : "))
# for i in range(1,row+1):
#     for k in range(row,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#        print("*",end=" ")
#     print()
# for i in range(1,row):
#     for k in range(0,i):
#         print(" ",end="")
#     for j in range(row,i,-1):
#        print("*",end=" ")
#     print() 



rows=int(input())
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print("*",end=" ")
    print()    