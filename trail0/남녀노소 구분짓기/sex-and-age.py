gender_id = int(input())
age = int(input())

if gender_id == 0:
    if(age >= 19):
        print("MAN")
    else:
        print("BOY")

else:
    if(age >= 19):
        print("WOMAN")
    else:
        print("GIRL")