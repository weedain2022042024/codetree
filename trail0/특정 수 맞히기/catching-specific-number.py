while True:
    num = int(input())
    if num == 25:
        print("Good")
        break
    
    if num < 25:
        print("Higher")
        continue
    if num > 25:
        print("Lower")
        continue