from math import reduce


squared = lambda num : num * num

print(squared(2))

addTwo = lambda num: num + 2


###################

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))


num_count = reduce(lambda acc, curr: acc + curr, numbers)

print(num_count)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob']

char_count =  reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)