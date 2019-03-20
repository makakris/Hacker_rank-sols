def nsum(x):
    return (x*(x+1))/2
a=[11,12,13,14,16,17,18,19,20]
s1=10
s2=20
print(nsum(s2))
print(nsum(s1))
print(sum(a))
print((nsum(s2)-nsum(s1))-sum(a))