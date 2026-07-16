
#TUPLE which is
#Imutable , ordered
#tu=(10,20,20,30,40)
#print(tu)
#two built-in methods 1)count 2)index
#print(tu.count(20))
#print(tu.index(30))



#QUESTION : PROBLEM Statement In a given array  we have to find second largest element from even-index and find the second 
# smallest element from odd index list and consider 0 as even index.
# li = [] 
# size = int(input("Enter the size of array : "))
# for i in range(0,size):
#     li.append(int(input()))
# print(li)    
# Even = []
# Odd = []
# Even.append(li[0])
# for i in range(1,size):
#     if i%2==0:
#         Even.append(li[i])
#     else:
#         Odd.append(li[i])    
# Even.sort()
# Odd.sort()
# print(f'Second largest element = {Even[len(Even)-2]}')
# print(f'Second smallest element = {Odd[1]}')  


#SET
#CANNOT HOLD DUPLICATE VALUES
#IT CONTAIN UNIQUE VALUES
#unordered

#s = {10,20,30,40,10}
#print(s)
# s.add(80)
# print(s)

#superset() checks whether a set contains all the elements of another set.if yes then true otherwise false
# s1 = {1,2,3,4,5}
# s2 = {2,3}
# print(s1.issuperset(s2))

#subset means all the elements of one set are present in another set. if yes then true otherwise false
# s1={20,30}
# s2={20,30,67,55,90}
# print(s1.issubset(s2))


rows=int(input())
start = 1
for i in range(1,rows +1):
    curr=start
    digitsum=0
    print()