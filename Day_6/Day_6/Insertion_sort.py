# def insertion(arr,size):
#     for i in range(1,size):
#         temp=arr[i]
#         j=i-1
#         while j>=0 and temp<=arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=temp
#     return arr    

# size=int(input("Enter the size : "))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(insertion(arr,size))    


#counting the vowels and consonants in the given string
str1=input("Enter the string : ")
count_vowels =0
count_cons=0
vowels="aeiouAEIOU"
for i in str1:
    if i in vowels:
        count_vowels+=1
    else:
        count_cons+=1
print("Vowels : ",count_vowels)    
print("Constonants : ",count_cons)        

     