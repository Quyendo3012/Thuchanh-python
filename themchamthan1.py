from re import S

s = input("Nhap S: ")
if s.find("!") == -1: s = s + "!!" 
elif s.count("!")%2 != 0: s = s + "!"
print("Chuoi S sau khi xu ly:",s)
