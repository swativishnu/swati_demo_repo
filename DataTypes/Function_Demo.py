# # Write a function func1() such that it can accept a variable length of  argument and print all arguments value
# def function(*arg):
#     for i in arg:
#         print(i)
#
#
# function(1, 2, 3, 4, 5)

# # Write a function calculation() such that it can accept two variables and calculate the addition
# # and subtraction of them. And also it must return both addition and subtraction
# # in a single return call
# def calculation(a, b):
#     return a + b, a - b


# print(calculation(12, 5))

# Create a function showEmployee() in such a way that it should accept employee name, and
# its salary and display both.
# If the salary is missing in the function call assign default value 9000 to salary
#
# def showEmployee(name, Salary=9000):
#     print("Employee ", name, "salary is", Salary)
#
#
# showEmployee("Ben", 9000)
# showEmployee("Ben")


def outerFunction(a, b):
    def innerFunction(c, d):
        return c + d

    value = innerFunction(a, b)
    return value + 5


print(outerFunction(10, 10))


# recurssive function to add 1 to 10

def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n


print(sum(10))

#
# def displayStudent(name, age):
#     print(name, age)
#
# displayStudent("Emma", 26)
#
# showStudent = displayStudent
# showStudent("Emma", 26)

# display even number in between 4,30

num_list = [num for num in range(4, 30)]
even_list = list(filter(lambda x: x % 2 == 0, num_list))
print(even_list)

print(list(range(4, 30, 2)))

from functools import reduce

# display largest number from list
aList = [4, 6, 8, 24, 12, 2]


def larger(a, b):
    if a > b:
        return a
    else:
        return b


largest = reduce(larger, aList)
print(largest)

print(max(aList))