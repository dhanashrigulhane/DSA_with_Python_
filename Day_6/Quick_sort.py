# def quick(arr,low,high):
#     if(low<high):
#         part=parition(arr,low,high)
#         quick(arr,low,part-1)
#         quick(arr,part+1,high)
#     return arr
# def parition(arr,low,high):
#     i=low
#     j=i-1
#     pivot=arr[high]
#     while(i<=high-1):
#         if(arr[i]<=pivot):
#             j+=1
#             #swapping
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp   
#             i+=1
#         else:
#             i+=1
#     #swapping
#     temp=arr[j+1]
#     arr[j+1]=arr[high]
#     arr[high]=temp
#     return j+1            
             
# size=int(input("Enter the size : "))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(quick(arr,0,size-1))    





#LINKED LIST
# class node:
#     def __init__ (self,data):
#        self.data=self.head
#        self.next=None
# class LinkedList:
#     head=None
#     def InsertAtBeg(self,data):

#         if self.head==None: 
#             node =node(data) 
#         else:
#             self.next=self.head
#             self.head=node 
#     def display(self):
#         if self.head==None :
#             print("Empty !")
#         else:
#             temp=self.head
#             while temp!=None:
#                 print(temp.data,end="->")   
#                 temp=temp.next
#             print()           
# choice=1
# ll=LinkedList()
# while choice!=0:
#     print("1.Insert at beg")
#     print("2.Display")
#     choice=int(input("Enter the choice :"))
#     if choice==1:
#         data=int(input("Enter data :"))
#         ll.InsertAtBeg(data)
#     elif(choice==2):
#         ll.display()




