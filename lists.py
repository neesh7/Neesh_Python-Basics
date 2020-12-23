computer_parts= ["mouse",
                 " keyboard",
                 " monitor",
                 " cpu",
                 "hardisk"]

for part in computer_parts:
    print(part)
print()
print(computer_parts[2])
print(computer_parts[0:3])
print(computer_parts[-1 ])
print("_"*80)
#lec 104 content
computer_parts[4] = "Baseball" #replacing single items
print(computer_parts)
computer_parts[3:4] = ["Bat"]  #using slices replacing multiple items in a list
print(computer_parts)
computer_parts[2:] = ["Makeup"]
print(computer_parts)