n = int(input('Nhap N duong: '))
tong = 0
t = 1
for i in range(1, n+1,1):
    t = t*i
    tong = tong + t
print("F("+ str(n) + ") =", tong)
