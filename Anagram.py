def wordcount(data):
    x=dict()
    for i in data:
        x[i]=x.get(i,0)+1
    return x
s1="pop"
s2="asff"
if wordcount(s1) == wordcount(s2):
    print("Anagram")
else:
    print("Not Anagram")