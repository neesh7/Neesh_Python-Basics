# print("what Would You Like to Eat")
# menu_choices = ["DOSA" , "IDLI" , "PAV BHAJI" , "SAMOSA" , "SWEETS"]
# print("1.DOSA\n2.IDLI\n3.PAV BHAJI\n4.SAMOSA\n5.SWEETS")
# choice= input("Your Choice")
# void=0
# for index in range(len(menu_choices)):
#     if menu_choices[index] == choice:
#         print("Item selected is {}".format(choice))
#     else:
#         print("Thank u It's Ok Come Again")
#         break
print("what would u like to eat")
print(" 1: Dosa \n 2: Idli \n 3:Pavbhaji \n 4:Samosa " )
while True:
    choice=input()

    if choice == "0":
        break
    elif choice in "1234":
        print("You choose {} in Meals".format(choice))
    else:
        print(" 1: Dosa \n 2: Idli \n 3:Pavbhaji \n 4:Samosa " )
else:
    print("Have a Good day")