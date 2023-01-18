n = input()
k = []
for i in n:
    if int(i) == 7 or int(i) == 4:
        k.append(i)

if len(k) == 4 or len(k) == 7:
    print("YES")
else:
    print("NO")