n,k = input().split()
n,k = int(n),int(k)

while k != 0 :
    if n % 10 == 0:
        n = n / 10
        k = k - 1
    else:
        n = n - 1
        k = k - 1
print(int(n)) 