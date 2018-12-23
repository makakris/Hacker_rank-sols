def string_rotate():
    S = input("Enter a string")
    C = input("Enter direction")
    R = int(input("Enter no. of rotations"))
    R=R-1
    if C=='c':
        print(S[R:]+S[:R])
    elif C=='a':
        print(S[-R:]+S[:-R])

    return    
