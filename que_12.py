n = int(input())
string = str(input())
count = 0
for i in range(len(string) - 1):
    if string[i] == string[i+1]:
        count = count + 1
print(count)


