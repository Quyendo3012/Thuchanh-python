N = int(input("N = "))

s = 0
for i in range(1, N+1):
    if N % i == 0:
        s += i
print("Tong cac uoc so cua", N, "la", s)
