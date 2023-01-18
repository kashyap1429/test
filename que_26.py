n = int(input())
a1 = []
b1 = []
count = 0

for i in range(n):
    a,b = input().split()
    a,b = int(a),int(b)
    a1.append(a)
    b1.append(b)

for i in range(n):
    if b1[i] - a1[i] >= 2:
        count = count + 1
print(count)
