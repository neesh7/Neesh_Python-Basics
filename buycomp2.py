availble_parts= ["Monitor",
                 "Mouse",
                 "Mouse Mat",
                 "keyboard",
                 "Hardisk",
                 "Hdmi cable"]
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
        # for parts in availble_parts:
        #     #print(parts) we also want numbering to be printed out so that we know which part is being selected
        #     print("{0}:{1}".format(availble_parts.index(parts)+1,parts))
        for number , parts in enumerate(availble_parts):
              print("{}:{}".format(number+1,parts))
        print("Press 0 to Finish")
    current_choice=input()
print(computer_parts)