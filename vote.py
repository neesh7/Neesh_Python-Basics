name = input("Plz Apna Naam Bataye")
age = int(input("Appka Age enter karein"))
print(age)
print()
if age >= 18:
    print("you are old Enough to Vote")
    print("Plz Put X in box")
else:
    print("Dear {} You Are not Eligible to vote".format(name))
    print("Plz come back After {} Years".format(18-age))
# we can also write same condition in other ways
if age < 18:
    print("{} Plz come back in {} Years".format(name, 18-age))
else:
    print("plz put a x in the box")

