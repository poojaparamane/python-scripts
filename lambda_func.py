# Write a Python program to sort tuples using Lambda.


# Write a Python program to square and cube every number in a given list of integers using Lambda

numbers = [1,2,3,4,5,6,7,8]

square = list(map(lambda x: x**2, numbers))
cubes = list(map(lambda x: x**3,numbers))

print("list", numbers)
print("square", square)
print("cubes", cubes)
# Write a Python program to count the even and odd numbers in a given list of integers using Lambda.

numbers= [1,2,3,4,5]

# numbers_even = list(map(lambda x: x % 2 ==0, numbers))
# numbers_odd = list(map(lambda x: x %2 !=0, numbers))

numbers_even = list(list(lambda x: x % 2 ==0, numbers))
numbers_odd = list(list(lambda x:%2 !=0, numbers))

print("even", numbers_even)
print("odd", numbers_odd)

# Write a Python program to add two given lists using map and lambda.