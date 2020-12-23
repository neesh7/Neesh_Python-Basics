#0 is considered as false so it can't be executed # as if statement excepts a Boolean expression
if 0:
    print("True")
else:
    print("False")
name = input("Tell Me your name")
if name:   # an empty string is considered as false so if we don't provide any name python will jump to else condition
    print("ok so Your name is {}".format(name))
else:
    print("Are you a Man with No Name!")
# for i in range (1,12):
#     print(i**2)