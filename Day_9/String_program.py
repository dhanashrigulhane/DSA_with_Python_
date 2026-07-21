#string=abc##def#hg
#output=###abcdefhg
str1=input("Enter the string : ")
hashes=""
chars=""
for char in str1:
    if char == '#':
        hashes+= '#'
    else:
        chars+= char
print(hashes + chars)       