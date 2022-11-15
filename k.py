import math
x = int(input())
y = math.ceil(x/2)

for row in range(y):
    for col in range(y+1):
        if col==0:
            print("*",end="")
        elif(col+row==y):
            print("*")
            break
        else:
            print(end=" ")

if(x%2==0):
    print("**")

for row in range(y-1):
    for col in range(y+1):
        if col==0:
            print("*",end="")
        elif(col-row==2):
            print("*")
            break
        else:
            print(end=" ")


end = input()
