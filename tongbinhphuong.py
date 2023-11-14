N = int(input("N = "))
s,t= 0,1
for i in range(1, N+1):
    t = i*i
    s = s + t
print ("P(" +str(N) + ") =", s)

'''i, s =1,0
while i <= N:
    s = s + i*i
    i += 1 
print("P(" + str(N) + ") =",s) '''
