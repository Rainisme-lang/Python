n = input("前:酸性多少 : ")
m = input("後:檢性多少 : ")

n = float(n)
m = float(m)

n = 10**(-1*n)
m = 20**(-1*(14-m))

if n*5 >= m*20 :
    h = (n*5 - m*20)/25
    count = 0
    while h<1 :
        h *= 10
        count+= 1
    print(count)
else :
    h = (m*20 - n*5)/25
    count = 0
    while h<1 :
        h *= 10
        count+= 1
    print(14 - count)