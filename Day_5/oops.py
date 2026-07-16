# class sipna:
#     a=10
#     b=20
#     def demo(self,a,b):
#         print(a,b)

# obj1=sipna()        
# obj=sipna()
# obj1.demo(50,60)
# print(obj.a)
# print(obj.b)    

# class sipna:
#     a=10
#     b=20
#     def demo(self,a,b):
#         self.a=a
#         self.b=b
# obj1=sipna()
# obj=sipna()    
# obj1.demo(30,40)
# print(obj.a)
# print(obj1.b) 
# 
#constructors
# class sipna:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# obj=sipna(50,100)
# print(obj.a)
# print(obj.b)           

#single inheritance
# class demo:
#     def add(self,a,b):
#         return a+b
# class calculations(demo):
#     def sub(self,a,b):
#         return a-b
# obj=demo()
# cal=calculations()
# print(cal.add(40,20))
# print(cal.sub(30,20))    
       
#Multiple inheritance
# class demo:
#     def add(self,a,b):
#         return a +b
# class demo1:
#     def sub(self,a,b):
#         return a-b
# class calculations(demo,demo1):
#     def mul(self,a,b):
#         return a*b 

# obj=demo()
# obj1=demo1()
# cal=calculations()
# print(cal.add(23,22))
# print(cal.sub(20,10))
# print(cal.mul(20,5))       

#MULTILEVEL INHERTIANCE
# class demo:
#     def add(self,a,b):
#         return a +b
# class demo1(demo):
#     def sub(self,a,b):
#         return a-b
# class calculations(demo1):
#     def mul(self,a,b):
#         return a*b 

# obj=demo()
# obj1=demo1()
# cal=calculations()
# print(obj1.add(23,22))
# print(cal.sub(20,10))
# print(cal.mul(20,5)) 


#ENCAPSULATION 
# class sipna:
#     a=10
#     def demo(self):
#         __b=10        #private member which can be access only through method 
#         print(__b)
# obj=sipna()
# print(obj.a)
# obj.demo()        


#POLYMORPHISM
# class sipna :
#     def add(self,a,b):
#         return a+b
# class sipna1(sipna):
#     def add(self,a,b,c):
#         return a+b+c
# obj=sipna()
# obj1=sipna1()
# print(obj.add(10,30))
# print(obj1.add(20,40,1))        



# class sipna:
#     def add(self):
#         print("sipna")
# class sipna1(sipna):
#     def add(self):
#         print("sipna1")
# class sipna2:
#     def add(self):
#         print("sipna2")
# obj=sipna()
# obj1=sipna1()
# obj2=sipna2()
# for i in obj,obj1,obj2:
#     i.add()        

#3 class list string int add fun 
# class interger:
#     def add(self,a,b):
#          return a+b 
# class string:
#     def add(self,a,b):
#         return a+b
# class list:
#     def add(self,a,b):
#         if 
#         return a+b
# obj=interger()
# obj1=string()
# obj2=list()
# print(obj.add(2,4))
# print(obj1.add("hii","hello"))
# print(obj2.add([1,2,3],[4,5,6]))        
