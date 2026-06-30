def details(a,b):
    print(a,b)
    print(f"my name is {a} and my age is {b}")

details("pooja", 27)
          

# 1. Write a Python function to find the maximum of three numbers.
def max(a,b,c):
    ma

# 2. Write a Python function to sum all the numbers in a list.
def sum(numbers):
    i = 0
    for num in numbers:
        i +=numbers
        print(i)
    sum([67,89,98])

# 3. Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for num in numbers:
        result *=num
    return result

nums = [1, 2,3,4,5]
print(multiply(nums))
# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(num):
    fact = 1
    for i in range(1,num):
        fact*=i
    print(fact)
fact(5)




# 5. Write a Python program to print the even numbers from a given list.

def even(numbers):
    for num in numbers:
        if num % 2 ==0:
            print(num)

nums = [1,2,3,4,5,6,7,8]
even(nums)