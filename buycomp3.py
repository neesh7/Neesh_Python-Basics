availble_parts= ["Monitor",
                 "Mouse",
                 "Mouse Mat",
                 "keyboard",
                 "Hardisk",
                 "Hdmi cable"]
current_choice="-"
computer_parts=[] #an empty list
# valid_choices= [str(i) for i in range(1, len(availble_parts)+1)]  #we used comphrehnsions there
# print(valid_choices)
valid_choices= []
for i in range(1,len(availble_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)
while current_choice != '0':
    if current_choice in valid_choices:
        index=int(current_choice)-1
        choosen_parts=availble_parts[index]
        if choosen_parts in  computer_parts: # if the thing is already in list these few line of codes will cause removel of them
            print("Removing  {}".format(current_choice))
            computer_parts.remove(choosen_parts)
            print("Your list now Contains {}".format(computer_parts))
        else:
            print("Adding  {}".format(current_choice))
            computer_parts.append(choosen_parts)
            print("Your list now Contains {}".format(computer_parts))
    else:#we will display menu and let user choose
        # for parts in availble_parts:
        #     #print(parts) we also want numbering to be printed out so that we know which part is being selected
        #     print("{0}:{1}".format(availble_parts.index(parts)+1,parts))
        for number , parts in enumerate(availble_parts):
            print("{}:{}".format(number+1,parts))
        print("Press 0 to Finish")
    current_choice=input()
print("S o,You Have These items in ur cart")
print(computer_parts)