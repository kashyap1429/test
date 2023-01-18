k,n,w = input().split()
k,n,w = int(k),int(n),int(w)

a = []
for i in range(1,w+1):
    a.append(k * i)

if sum(a)-n < 0:
    print(0)
else:
    print(sum(a)-n)