current_choice="-"
computer_parts=[] #an empty list
while current_choice != '0':
    if current_choice in "123456":
        print("Adding  {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("Monitor")
        elif current_choice == '2':
            computer_parts.append("Mouse")
        elif current_choice == '3':
            computer_parts.append("Mouse Mat")
        elif current_choice =='4':
            computer_parts.append("Keyboard")
        elif current_choice == '5':
            computer_parts.append("Hardisk")
        elif current_choice== '6':
            computer_parts.append("Hdmi Cable")
    else:#we will display menu and let user choose
        print("1:Monitor")
        print("2:Mouse")
        print("3:Mouse Mat")
        print("4:keyboard")
        print("5:Hardisk")
        print("6: Hdmi Cable")
        print("Press 0 to Finish")
    current_choice=input()
print(computer_parts)