Ia, Ib, Fa, Fb = map(int,input().split())
if Ia == Fa and Ib == Fb:
    print("0")
elif Ia != Fa and Ib == Fb:
    print("1")
elif Ia == Fa and Ib != Fb:
    print("2")
else:
    if Ia != Fa and Ib != Fb:
        if (Ia == Ib and Fa == Fb) or (Ia != Ib and Fa != Fb):
            print("1")
        else:
            print("2")