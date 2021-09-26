# # Given an input string, count occurrences of all characters within a string
# import collections
#
# str1 = "Apple"
# dict1 = {}
# for char in str1:
#     if char not in dict1.keys():
#         dict1[char] = 1
#     else:
#         dict1[char] += 1
#
# print(dict1)
#
# str1 = "Apple"
# countDict = dict()
# for char in str1:
#   count = str1.count(char)
#   countDict[char]=count
# print(countDict)
#
# dict2 = collections.Counter(str1)
# print(dict2)

# # Find the last position of a substring “Emma” in a given string
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print(str1.rfind("Emma"))
#
#
# # Split a given string on hyphens into several substrings and display each substring
# str1 = "Emma-is-a-data-scientist"
# list1 = str1.split("-")
# for element in list1:
#     print(element)

# # Remove empty strings from a list of strings
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# new_str_list = list(filter(None, str_list))
#
# print("After removing empty strings")
# print(new_str_list)
#
# # Remove special symbols/Punctuation from a given string
# str1 = "/*Jon is @developer & musician"
# str2 = ""
# for char in str1:
#     if char.isalnum() or char == " ":
#         str2 = str2 +char
#
#
# print(str2)

# Removal all the characters other than integers from a string
import string

str1 = 'I am 25 years and 10 months old'
new_str = "".join([item for item in str1 if item.isdigit()])
print(new_str)

# for char in str1:


str1 = "/*Jon is @developer & musician!!"
new_str = ""
for char in str1:
    if char in string.punctuation:
        str1 = str1.replace(char, '#')

print(str1)
