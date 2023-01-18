n = int(input())
s = input()
k = []
l = []

for i in s:
    if i == 'A':
        k.append(i)
    else:
        l.append(i)

if len(k) > len(l):
    print("Anton")
elif len(k) < len(l):
    print("Danik")
else:
    print("Friendship")
