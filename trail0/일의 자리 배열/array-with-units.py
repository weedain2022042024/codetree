result = list(map(int, input().split()))

for i in range(8):
    num = (result[i] + result[i+1]) % 10
    result.append(num)

for i in result:
    print(i, end=' ')