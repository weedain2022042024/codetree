arr = []
cnt_1 = 0
cnt_2 = 0

for i in range(1, 11):
    arr.append(int(input()))
    
for i in arr:
    if (i % 3 == 0):
        cnt_1 += 1
    if (i % 5 == 0):
        cnt_2 += 1
    else:
        continue

print(cnt_1, cnt_2)