alpha = input()

arr = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for i in arr:
    if (i[2] == alpha) or (i[3] == alpha):
        print(i)
        cnt += 1

    else:
        continue
    #print(i, end=' ')
print(cnt)