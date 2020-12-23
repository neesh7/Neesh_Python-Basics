 #indexing
 #negative indexing concept
         #01234567890123
parrot = 'NORWEGIAN BLUE'
print(parrot)
# Indexing : By using this we can print selected Strings
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[0])
# This whole output "We Win" can be printed simply by using slicing
print(parrot[3:5] + " " + parrot[3:7:3] + parrot[8])
print()

print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print()
print()
#Slicing in python

print(parrot[6:0])
print(parrot[2:4])
print(parrot[ :11])  # By default if the start value is left empty then it becomes 0.
print(parrot[2: ])   # By default if the stop value is left empty then it becomes maximum or the last index of the string.
print(parrot[:2])
print(parrot[:6]+parrot[6:])
print(parrot[ : ])  # This will print the whole string