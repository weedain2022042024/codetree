A, B = map(int, input().split())
num_1 = 0
num_2 = 0

if A < B:
    num_1 = 1 
else:
    num_1 = 0

if A == B:
    num_2 = 1 
else:
    num_2 = 0

print(num_1, num_2, end=" ")