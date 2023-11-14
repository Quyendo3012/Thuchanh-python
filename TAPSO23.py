n = int(input("N = "))
i,j,k=0,0,0
a = [1]
while (k<n):
    if a[i]*2+1 < a[j]*3+1:
       a.append(a[i]*2+1) 
       i,k=i+1,k+1
    elif a[i]*2+1 != a[j]*3+1:
        a.append(a[j]*3+1)
        j,k=j+1,k+1
    else:  j+=1
print(f"{n} so dau tien cua N23:",end="")
for i in range(n): 
    print(f" {a[i]}",end= "" if i<n-1 else "\n")