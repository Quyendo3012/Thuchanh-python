a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if a <=0 or b <= 0 or c <= 0 or a+b <= c or b+c <= a or a+c <= b: print("Khong phai tam giac")
else : print("Dung la tam giac")
