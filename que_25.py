n = int(input())

a = [int(x) for x in input().split()]

if a.count(1) >= 1:
    print("HARD")
else:
    print("EASY")
