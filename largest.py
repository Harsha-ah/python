a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
    print(f"largest number is :{a}")
elif b>a and b>c:
    print(f"largest number is:{b}")
else:
    print(f"largest number is:{c}")