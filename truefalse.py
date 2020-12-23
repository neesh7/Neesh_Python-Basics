day = input("Enter the day")
temperature = int(input("What's Temp Today"))  # HERE we used int input because temperature is an integer value
x = input("""Is it Raining Enter 'True' or 'False'""")
raining = x
if day == 'Saturday' and temperature > 27 or not raining:
    print('Go Swim')
else:
    print("learn Python")
