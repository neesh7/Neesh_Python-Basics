name = input("Plz Apna Naam Bataye ")
age = int(input("Appka Age enter karein "))
print(age)
print()
# if age >=18 :
#     print("you are old Enough to Vote")
#     print("Plz Put X in box")
# else:
# print("Plz come back After {} Years".format(18-age))
# we can also write same condition in other ways
if age < 18:
    print("You are not Eligible to vote so, Plz come back in {} Years".format(18 - age))
elif age >= 900:
    print("oh!!! {} plz die".format(name))
else:
    print("plz put a x in the box")
