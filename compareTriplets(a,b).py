def compareTriplets(a, b):
    x,y=0,0
    for i in range(0,3):
        if a[i]>b[i]:
            x=x+1
        elif a[i]<b[i]:
            y=y+1
        else:
            continue
    return [x,y]
