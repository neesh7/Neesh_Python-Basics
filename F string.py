name = "tim's"
age = 23
print("His age is {0}".format(age))
# or using .format
print(name + " Age is " + "{0}".format(age))
# or
print("{} Age is {}".format(name, age))
# or , using F-string (Formatted string)
print((name + f" age is {age} Years Old "))
# or using str()
print("Tims age is " + str(age))
# concept of pi
print(f"Pi is approx {22 / 7:12.50f}")
# or we can do this way
pi = 22 / 7
print(f"pi is approx {pi:12.50f}")
# These all are basically string formatting methods in Python
