str = list(input())

for i in str:
    str[1] = 'a'
    str[(len(str))-2] = 'a'
    print(i, end='')