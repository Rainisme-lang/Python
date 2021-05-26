n = input("幾層金字塔 : ")
n = int(n)
for i in range(n):
    s=""
    for j in range(n-1-i):
        s += ' '
    for j in range(2*i+1):
        s += '*'
    print(s)

print("方法2 : ")
for i in range(n):
    print(' '*(n-1-i) + '*'*(2*i+1))