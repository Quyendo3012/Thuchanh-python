n = int(input("N = "))
import math

def int_squareroot(d):
    left, right = 0, d
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == d:
            return mid
        elif mid * mid > d:
            left, right = left, mid - 1
        else:
            left, right = mid + 1, right
    return -1

if n < 0 or n % 2 != 0:
    print("N khong phai la so fibonacci chan")
else:
    a = 5*n*n + 4
    x1 = int_squareroot(a)
    b = 5*n*n - 4
    x2 = int_squareroot(b)
    if a == x1*x1 or b == x2*x2:
        print("N la so fibonacci chan")
    else:
        print("N khong phai la so fibonacci chan")
