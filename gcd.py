a=int(input("enter first num:"))
b=int(input("enter second num:"))
if a<b:
    min=a
else:
    min=b
    gcd=1
for i in range(1,min+1):
    if a%i==0 and b%i==0:
         gcd=i
print(f"the gcd of {a} and {b} is {gcd}")

