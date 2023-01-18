a = str(input())

a = list(a)

k = []
for i in a:
    if i != '+':
        k.append(i)

k = sorted(k)

result = ['+'] * (len(k) * 2 - 1)
result[0::2] = k

l = ''.join(result)

print(l)





# a = [1,3,2]
# a.sort()
# print(a)