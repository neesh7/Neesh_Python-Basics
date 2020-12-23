empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
#by concenating 2 lists
numbers = even + odd
print(numbers)
sorted_numbers = sorted(numbers)
print()
digits = sorted("932536347")
print(digits)
print()
digits = list("932536347")   #this time same list will be created but it is'nt sorted
print(digits)
print()
more_numbers = list(digits)
print(more_numbers)
print(digits is more_numbers)  #  this will result output as false cz i know it's the same elements in those 2 lists but those are not same list those are different list having identical elements
print(digits == more_numbers) # by this we are checking if the two list containing identical elements
#another way to copy a list is slicing
print(numbers)
new_numbers = numbers [ : ]
print(new_numbers)
print()
#best method to copy a list is copy method
abc = ["comp" , "jack", "ryan",2,3,4]
xyz = abc.copy()
print(abc)
print(xyz)