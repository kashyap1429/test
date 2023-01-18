t = int(input())
a1 = []

for i in range(t):
    k = 0
    a,b = input().split()
    a,b = int(a),int(b)
    if a % b == 0:
        a1.append(0)
    else:
        if a > b:
            a1.append(b - (a % b))
        else:
            a1.append(b - a)
for i in a1: 
    print(i)
