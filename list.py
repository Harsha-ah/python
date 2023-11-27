list1=[2,4,-6,-8,9,7]
list2=[i for i in list1 if (i>0)];
print(f"positive list={list2}")
#square
list1=[2,3,4]
list2=[i**2 for i in list1]
print(f"square is={list2}")
#vowels
word=input("enter a word:")
listvowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels are:{listvowel}")
#ordinal value
text=input("enter any character:")
ordinals=[ord(i) for i in text]
print(ordinals)