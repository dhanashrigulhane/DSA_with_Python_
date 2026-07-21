#factorial
# num = int(input())
# fact = 1
# for i in range ( 2, num+1):
#     fact= fact * i
# print(fact)


def calcu(num):
    if num==1:
        return num
    return num*calcu(num-1)
num=int(input("Enter the number :"))
print(calcu(num))


