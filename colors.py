color=[]
n=int(input("enter the tottal number of colors:"))
print("colors:")
for i in range(n):
    ch=input()
    color.append(ch)
    print(f"first color is:{color[0]}\n last color is:{color[-1]}")