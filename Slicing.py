  #concept of slicing is justn an advance version of indexing as we introduce limits to it .
  #01234
x="Neesh"
  #54321  All Are basically Negative
print()
print(x)
print(x[4])    #This is called  positive indexing
print(x[-1])   #This is called  Negative indexing
print()
#forward slicing or Positive slicing - introduction of limits into indexing is slicing

print(x[1:3])     #ee   Using Forward or positive slicing
print(x[-5:-3])     #ee   using negative slicing or what i call is Backward slicing
print(x[:])
#using step Values
print(x[0:4:2])
print(x[0:3:])
print()
number="1.221:222!453,333"
print(number[1::4])   #it will print seprators till end as no stop value is providedd
#other way to write same code
z=number[1::4]
print(z)
values="".join(char if char not in z else""for char in number).split()
print([int(val) for val in values])
#Negative step slicing
w="abcdefghijklmnopqrstuvwxyz"
print(w[25:0:-1])
print(x[4::-1])
print(w[16:13:-1])   #qpo
print(w[4::-1])     #edcba