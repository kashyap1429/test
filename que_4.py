a,b = input().split()
a,b = int(a),int(b)

k = input().split()
p = []
for ele in k:
    if int(ele) >= int(k[b-1]) and int(ele) > 0:
        p.append(ele)
if len(p) == 0:
    print(0)
else:
    print(len(p))