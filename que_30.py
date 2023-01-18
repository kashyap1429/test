a = input()
b = input()

a1 = []
b1 = []

for i in a:
    a1.append(int(i))
for i in b:
    b1.append(int(i))

k = []

for i in range(len(a)):
    if a1[i] + b1[i] == 0:
        k.append(0)
    elif a1[i] + b1[i] == 1:
        k.append(1)
    else:
        k.append(0)

k1 = []

for i in k:
    k1.append(str(i))

k2 = ''.join(k1)
print(k2)