name = input("what's ur name Dear ")
age = int(input("Whats ur age "))
if 18 <= age <= 31:
    print("Welcome {} to the Holiday \nHave some Wine!!".format(name))
elif age < 18:
    print("Sorry {} Yor are not eligible for holiday please try after {}".format(name, 18-age))
else:
    print("Sir You are too aged")
