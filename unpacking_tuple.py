a=b=c=d=e=f= 42
print(a)
print(f)
print("_"*80)
x, y, z = 2, 7, 81
print(x)
print(y)
print(z)
print("Unpacking a Tuple")
data = 2, 7, 93  # data represents tuples
x, y, z = data  # here data is a tuple and x, y, z gets the value from a tuple called data . but xyz are not a tuple .
print(x)   # cz u can't have tuples in the left hand side of an assignment . becz tuples are immutable
print(y)
print(z)
print("Unpacking a List")
data_list = [1, 33, 87]
x, y, z = data_list  # this step is called unpacking of list as x,y,z variables gets the values from our data list
print(x)
print(y)
print(z)
# Suppose if we try to Append any item to list then unpacking of them causes an error
print("_"*80)
data_list.append(19)
print(data_list)
x, y, z =  data_list
print(x)   # these print x y z statement will cause an error because lsit contains 4 items and we are unpacking in 3 variables.
print(y)   # it's quiet not possible and will cause an error
print(z)   # but in tuple such errors doesnt appear cz items can't be appended to tuples
