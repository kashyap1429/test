n = int(input())
string = []
add = 0

for i in range(n):
    a = input()
    string.append(a)

for j in string:
    if j.count('1') >= 2:
        add += 1
print(add)