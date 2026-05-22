A, B = map(int, input().split())
num = A

while True:
    if num > B:
        break

    print(num, end=" ")

    if num % 2 == 1:
        num = num * 2
        
    else:
        num += 3
    