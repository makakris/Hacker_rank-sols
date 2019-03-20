def is_triangle(a,b,c):
    if (a+b>c) and (b+c>a) and (a+c>b):
        return ("Valid Triangle")
    else:
        return ("Invalid Triangle")
x=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(x)-2):
    print(x[i],x[i+1],x[i+2],"is",is_triangle(x[i],x[i+1],x[i+2]))
