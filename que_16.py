string = str(input())

a = []
b = []
for i in string:
    if ord(i) in range(65,91):
        a.append(i)
    else:
        b.append(i)

if len(b) < len(a):
    print(string.upper())
else:
    print(string.lower())
