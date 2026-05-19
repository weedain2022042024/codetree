a, b, c = map(int, input().split())

sum = a + b + c
avg = int(sum / 3)

num = int(sum - avg)

print(sum, avg, num, sep='\n')