# def function(a,b):
#     return(a+b)
# function(10,20)



# def demo(*args):
#     c=0
#     for i in args:
#         c+=i
#     return c

# print(demo(10,20,30,40))


# def demo(**kwargs):
#     print(kwargs)

# demo(a="Khushi",b="dhanu",c="Aastha")



#take three inputs from user in the range 10 to 20
# def fun(num1,num2,n):
#     sum1=0
#     sum2=0
#     sum=0
#     for i in range(num1,num2+1):
#         if i%3==0:
#             sum1+=i
#         else:
#             sum2+=i
#     print("The sum of the number which is divisible by 3 is ",sum1)
#     print("The sum of the number which is not divisible by 3 is ",sum2)
#     print("The difference between the two sum is ",sum2-sum1)

# start=int(input("Enter starting num : "))
# end=int(input("Enter the ending number : "))
# num=int(input("Enter the number to divide : "))
# fun(start,end,num)    



#QUESTION aabbbcccd=string output=a2b3c3d        
# def demo(str1):
#     str2=""
#     for i in str1:
#         if i not in str2:
#             if str1.count(i)>1:
#                 str2+=i
#                 str2+=str(str1.count(i))
#             else:
#                 str2+=i 
#     print(str2)  

# str1=input("enter the string : ")
# demo(str1)               


