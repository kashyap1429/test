x = int(input())

if x in range(1,6):
    print(1)
else:
    i = 1
    while x not in range(1,6):
        x = x - 5
        i = i + 1
    print(i) 
