# numbers = [1,45,43,31,74]
# for number in numbers:
#     if number % 8 == 0:
#         print("This is unacceptable")
# else: #Keep in mind about indentations  cz it's just the indentiation which seprates eveerything
#     print("The numbers are acceptable")
asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]
#
# for asteroid in asteroids:
#     if asteroid == 9617:
#         print("Grahamchapman")
#     elif asteroid == 9618:
#         print("Johncleese")
#     elif asteroid == 9619:
#         print("Terrygilliam")
#         break
#     elif asteroid == 9620:
#         print("Ericidle")
#     elif asteroid == 9621:
#         print("Michaelpalin")
#     else:
#         print("Terryjones")
# else:
#     print("MontyPython")
choice = None

while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        break

    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")