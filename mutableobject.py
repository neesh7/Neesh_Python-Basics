shopping_list= ["eggs",
                "milk",
                "Buiscuits",
                "Bread",
                "Sandwich"]
another_list=shopping_list
print(id(shopping_list))
print(id(another_list))
print(shopping_list)
#Let's try to mutate our list this time and see what happens
a=b=c=d=e=f=g= another_list
print(a)
print("Add cream")
a.append("Cream")
print(b)
x=shopping_list
print(x)

