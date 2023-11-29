def countChar(inputString):
    Count={}
    for char in inputString:
     if char in Count:
       Count[char]+=1
     else:
       Count[char]=1
    return Count
str1=input("enter a string:")
result=countChar(str1)
print(result)
