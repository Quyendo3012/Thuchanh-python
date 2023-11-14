n = int(input("N = "))
mu = 2**n
def tong(n): 
    tongg = 0
    while n > 0:   
        tongg += n%10
        n = n//10
    return tongg
print("Tong =",tong(mu))