t = int(input())
k = []
for i in range(t):
    a = input()
    a1 = str(a)
    a2 = len(a1)
    a3 = [int(x) for x in a1]
    k1 = []
    for i in a3:
        if i != 0:
            k1.append(i * (10 ** (a2 - 1 - a3.index(i))))
    k.append(k1)

for i in k:
    print(len(i))
    for j in i:
        print(j,end=" ")
    print()