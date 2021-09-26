# Generate 6 digit random secure OTP
import random
import secrets
#
# #Getting systemRandom class instance out of secrets module
# import string
#
# secretsGenerator = secrets.SystemRandom()
#
# print("Generating 6 digit random OTP")
# otp = secretsGenerator.randrange(100000, 999999)
#
# print("Secure random OTP is ", otp)
#
# # Pick a random character from a given String
# str1 = "andhiomx"
# char1 = random.choice(str1)
# print(char1)
#
#
# # Generate  random String of length 5
# str1 = ""
# for i in range(5):
#     char1 = random.choice(string.ascii_letters)
#     str1 += char1
#
# print("string of length 5", str1)

#  Generate a random Password which meets the following conditions
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

# def randomPassword():
#     randomSource = string.ascii_letters + string.digits + string.punctuation
#     password = random.sample(randomSource, 6)
#     password += random.sample(string.ascii_uppercase, 2)
#     password += random.choice(string.digits)
#     password += random.choice(string.punctuation)
#
#     passwordList = list(password)
#     random.SystemRandom().shuffle(passwordList)
#     password = ''.join(passwordList)
#     return password
#
# print ("Password is ", randomPassword())
#
#
#  Calculate multiplication of two random float numbers
# Note:
# First random float number must be between 0.1 and 1
# Second random float number must be between 9.5 and 99.5

first_num = random.random()
second_num = random.uniform(9.5, 99.5)
print(first_num * second_num)


# Generate random secure token of 64 bytes and random URL

print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))

# Exercise 9: Roll dice in such a way that every time you get the same number
dice = [1, 2, 3, 4, 5, 6]
for i in range(5):
    random.seed(1)
    print(random.choice(dice))

