# for i in range(5):
#     print(i)
# else:
#     print("done!")
#
#
# # print prime number in a range
# def is_prime(num):
#     for i in range(2, num):
#         if (num % i == 0):
#             return False
#     else:
#         return True
#
#
# start = 25
# stop = 50
# for num in range(start, stop):
#     if is_prime(num):
#         print(num)

# first = 0
# second = 1
# print(first, second, end=" ")
# for i in range(8):
#     third = first + second
#     print(third, end=" ")
#     first, second = second, third
#
# num = -2
# factorial = 1
# if num < 0:
#     print("factorial of negative number does not exist")
# elif num == 0:
#     print("Factorial if 0 is 1")
# else:
#     for i in range(1, num+1):
#         factorial *= i
#     print(factorial)
#
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for num in my_list[1::2]:
#         print(num, end=" ")
#
# input_number = 6
# for num in range(1, input_number+1):
#     print(f" current number is : {num}  and the cube is {num**3}")

# number_of_terms = 5
# num = "2"
# sum = 0
# for i in range(1, number_of_terms+1):
#     print(num*i, end=" ")
#     sum += int((num*i))
# print(sum)

# for i in range(1, 6):
#     print("*" * i)
# for i in range(4, 1, -1):
#     print("*" * i)


def fibonacci_series(n):
    first = 0
    second = 1
    print(0)
    print(1)
    for _ in range(2, n):
        third =first +second
        print(third)
        first, second = second , third


fibonacci_series(100)