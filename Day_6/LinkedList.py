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




