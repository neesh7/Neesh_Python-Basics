available_exits = ["North","South","East","West"]
choosen_exits=""
while choosen_exits not in available_exits:
    choosen_exits=input("plz enter a direction:")
    if choosen_exits.casefold()=="quit":
        print("Game Over")
        break
else:
    print("aren't u intrested in getting out")
# for i in range(1,100):
#     print(i)
#     if i>0 and i%11==0:
#         print("Our no is {}".format(i))
#         break