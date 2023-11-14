n = int(input('N = '))
sum = 0
temp = 0
for i in range(1, n+1):
    temp = temp + i
    sum = sum + (temp)**0.5
print("F("+str(n)+") =", '{:.7f}'.format(sum))

