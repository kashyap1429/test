n = int(input())
a1 = []
b1 = []
c = 0
max = 0
for i in range(n):
    a,b = input().split()
    a,b = int(a),int(b)
    a1.append(a)
    b1.append(b)

for i in range(n):
    c = c + b1[i] - a1[i]
    if c > max:
        max = c

print(max)
