# def bubble(arr,size):
#     for j in range(size):
#         for i in range(0,size-1):
#             if (arr[i+1]< arr[i]):
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp
#     return arr        
# size=int(input("Enter the size : "))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))                

#OPTIMIZE CODE
# def bubble(arr,size):
#     for j in range(size):
#         flag=False
#         print(f'pass {j}:')
#         for i in range(0,size-1):
#             print(f'IT {i}:',end="")
#             print(arr)

#             if (arr[i+1]< arr[i]):
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp

#         if flag==False:
#                 break    
#     return arr        
# size=int(input("Enter the size : "))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))                


# def selection(arr,size):
#     for j in range(0,size-1):
#         min=j
#         for i in range(j+1,size):
            
#             if(arr[min]>arr[i]):

#                 min=i
#             #swapping
#         temp=arr[j]
#         arr[j]=arr[min]
#         arr[min]=temp
#     return arr 
# size=int(input("Enter the size : "))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(selection(arr,size))                
   
            