import math
a=[43,51,12,345,1244]
for i in a:
    for j in range(2,int(math.sqrt(i))):
        if i%j == 0:
            print("Not Prime")
            print(i,j,"*",i//j)
            break
    else:
        print("Prime")