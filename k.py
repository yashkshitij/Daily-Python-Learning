import math
x=int(input())
if(x%2==0):
    y=int(x/2)
else:
    y=math.ceil(x/2)
print(y)
for row in range(y):
    for col in range(y+1):
        if col==0:
            print("*",end="")
        elif(col+row==y):
            print("*",end="")
        else:
            print(end=" ")
        if col==y:
            print()
if(x%2==0):
    print("**")
for row1 in range(y-1):
    for col1 in range(y):
        if col1==0:
            print("*",end="")
        elif(col1-row1==2):
            print("*",end="")
        else:
            print(end=" ")
        if col1==y-1:
            print()

end = input()
