#same length
list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
if len(list1)==len(list2):
 print("a.the list have the same length")
else :
 print("a.the list have different length")

 #list have same sum
 print(f"b.sum of list1:{sum(list1)}& sum of list2 :{sum(list2)}")
 if sum(list1)==sum(list2):
  print("the list of sum to the same value")
 else:
  print("the list doesnt match the sum")

  #common values
  common_values=set(list1)&set(list2)
  if common_values:
   print(f"common values in both lists:{common_values}")
  else:
   print("there are no common values in both lists")