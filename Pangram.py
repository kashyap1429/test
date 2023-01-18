n = int(input())
s = str(input())

s1 = s.lower()
s2 = set(s1)

if len(s2) == 26:
    print("YES")
else:
    print("NO")