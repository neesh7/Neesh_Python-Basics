for i in range(1, 13):
    print("No. {0} Squared is {1} and cubed is {2}".format(i, i**2, i**3))
    # It prints the no and its square and its cubes
    # Now We will Use string Formatting in order to make our output more visible to ourselves
print("-"*80)
for i in range(1, 13):
    print("No. {0:2} Squared is {1:4} and cubed is {2:4} " .format(i, i**2, i**3))

print("_________________________________"*2)
for i in range(1, 13):
    print("No. {:2} Squared is {:4} and cubed is {:4} " .format(i, i**2, i**3))
