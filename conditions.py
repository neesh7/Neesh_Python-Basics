age=int(input("How old are u  "))
#if age>=16 and age<=65:
if 16 <= age <= 65:
    print("Enjoy Good day at work")
else:
    print("Enjoy Ur Free time")
print("_" * 80)
# program 2
# if 16<=age<=65:    instead of writing this we can use concept of range there in order to evaluate this condition easily
if age in range(16,66):
    print("Enjoy Good day At Work")
else:
    print("Enjoy ur Free Time")
print("_" * 80)
# Program 3
if age<16 or age>65:
    print("Enjoy ur free time")
else:
    print("Enjoy Good Day At Work")