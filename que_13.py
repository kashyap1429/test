a,b = input().split()
a,b = int(a),int(b)
i = 0
while a <= b:
    a = a * 3
    b = b * 2
    i = i + 1
print(i)