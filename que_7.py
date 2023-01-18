k = []
for j in range(5):
    a,b,c,d,e = input().split()
    a,b,c,d,e = int(a),int(b),int(c),int(d),int(e)
    k.append(a)
    k.append(b)
    k.append(c)
    k.append(d)
    k.append(e)

for i in k:
    if i == 1:
        k[i] = 0
print(k)    

    