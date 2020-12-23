empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
#by concenating 2 lists
numbers = even + odd
print(numbers)
numbers2 = [even, odd]
print(numbers2)  #numbers2 is a list which contains 2 more lists inside it.
for number_list in numbers2:
    print(number_list)

    for value in number_list:
        print(value)