A, B, C =map(int,input().split())
if(A == B and C != A):
    print("C")
elif(A == C and B != A):
    print("B")
elif(B == C and B != A):
    print("A")
else:
    print("*")