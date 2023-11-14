
N = int(input("N = "))
i, s =1,0
while i <= N:
    s = s + i*i
    i += 1 
print("P(" + str(N) + ") =",s) 
