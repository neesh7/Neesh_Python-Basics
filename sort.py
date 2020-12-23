a=[1,2,3,4,5,6]
b=[6,7,8,9]
print(a)
print(b)
#we will now use extend method in order to pass value of a to b
b.extend(a)   #extend is applied on b
print(b)  #now we see our output is'nt sorted so we can use sort method in order to sort our output
b.sort()
print(b) #as we sorted our output let's observe the change in our output
b.sort(reverse=True)  #we can also sort it into a reverse order using reverse sort
print(b)