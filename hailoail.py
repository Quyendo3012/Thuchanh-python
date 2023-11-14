n = int(input("Nhap N: "))
A, B = list(), list()
dem = 0
for i in range(1, n+1):
    x = input("Nhap gia tri thu %d: " % i)
    try: 
        A.append(int(x))
        dem += 1
    except:
        try: 
            A.append(float(x))
            dem += 1
        except: B.append(x)  
if dem>0:
    s = 0
    for i in A:
        s += i
    print("Tong cac phan tu cua A =", s)
print("B =", B)