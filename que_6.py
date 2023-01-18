x = 0

n = int(input())

for i in range(n):
    a = input()
    if (a.count('+') == 2 or a.count('-') == 2) and a.count('X') == 1:
        if a == '++X' or a == 'X++' :
            x = x + 1
        else:
            x
        if a == '--X' or a == 'X--':
            x = x - 1
        else:
            x
print(x)