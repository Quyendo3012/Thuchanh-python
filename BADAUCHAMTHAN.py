n=input("Nhap chuoi: ")
if n.endswith('!!!') == 1:
    print("Chuoi sau khi bo sung dau cham than: '"+n+"'")
elif n.endswith('!!') == 1:
    print("Chuoi sau khi bo sung dau cham than: '"+n+"!'")
elif n.endswith('!') == 1:
    print("Chuoi sau khi bo sung dau cham than: '"+n+"!!'")
else:
    print("Chuoi sau khi bo sung dau cham than: '"+n+"!!!'")
