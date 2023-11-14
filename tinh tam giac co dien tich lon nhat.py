from math import*
A = float(input("Do dai A = "))
B = float(input("Do dai B = "))
C = float(input("Do dai C = "))
D = float(input("Do dai D = "))
def ktTamGiac(a,b,c):
    if a+b>c and b+c>a and c+a>b: 
        return True
    return False
def S_TamGiac(a,b,c):
    p = (a+b+c)/2
    S = sqrt((p-a)*(p-b)*(p-c)*p)
    return S
list=[]
if ktTamGiac(A,B,C):
    S1 = S_TamGiac(A,B,C)
    list.append(S1)
if ktTamGiac(A,B,D):
    S2 = S_TamGiac(A,B,D)
    list.append(S2)
if ktTamGiac(D,B,C):
    S3 = S_TamGiac(D,B,C)
    list.append(S3)
if ktTamGiac(A,D,C):
    S4 = S_TamGiac(A,D,C)
    list.append(S4)    
    
Smax = max(list) 
if len(list) == 0:
    print("Ket qua = -1")
else: print("Ket qua = %.3f" %Smax)




