n = int(input())

if n == 1:
    print("I hate it")
elif n == 2:
    print("I hate that I love it")
else:
    if n % 2 == 0:
        k = ["I hate that"] * (n//2)
        k1 = ["I love that"] * (n//2)
        k2 = " I love it"
        k3 = []
        for i,j in zip(k,k1):
            k3.append(i)
            k3.append(j)

        k3.pop(-1)

        k4 = " ".join(k3) + k2
        print(k4)

    else:
        l = ["I hate that"] * (n//2)
        l1 = ["I love that"] * (n//2)
        l2 = " I hate it"
        l3 = []

        for i1,j1 in zip(l,l1):
            l3.append(i1)
            l3.append(j1)

        l4 = " ".join(l3) + l2

        print(l4)
