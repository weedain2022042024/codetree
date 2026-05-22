arr = []


while True:
    num = int(input())
    if num == 0:
        break
    arr.append(num)

for i in arr:
    print(i, sep='\n')
