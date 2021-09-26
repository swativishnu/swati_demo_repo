# """
# append  insert extend  copy count ,pop,clear, reverse, sort, index
# """
# list1 = [1, 2, 3, 4, 5]
# print(list1)
# #list1.append([7, 8])
# print(list1)
# list2 = [344, 56, 78, 7880]
# list1.extend(list2)
# print(list1)
# count_of_list = list1.count(1)
# print(count_of_list)
# # index returns index of element
# print(list1.index(1))
#
# # insert at particular index (index,value)


# list1.insert(2, 300)
# print(list1)
 # Pop removes last element from the list
# # list1.pop()
# # list1.pop()
# # list1.pop()
# # list1.pop()
# # # list1.pop()
# # list1.pop()
# print("After pop")
# print(list1)
#
# list1.remove(4)
# print("After remove", list1)
#
# copied_list = list1.copy()
# copied_list.insert(1, "50Ps")
#
# print(copied_list)
# list1.sort()
# print("sorted list", list1)


# #concatenate two list
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = []
# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])
#
# print(list3)
#
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)
#
# aList = [1, 2, 3, 4, 5, 6, 7]
# sqr_list = list(num**2 for num in aList)
# print(sqr_list)

# Given a two Python list. Iterate both lists simultaneously such that
# list1 should display item in original order and list2 in reverse order
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# l2_len=len(list2)
# for i in range(len(list1)):
#     print(list1[i],list2[-1-i])
#
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

# # remove empty string from list
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for val in list1:
#     if val:
#         pass
#     else:
#         list1.remove(val)
# print(list1)
# #
# # replace first 20 by 200
# num_list = [5, 10, 15, 20, 25, 50, 20]
# numbers = [2, 56, 8, 1]
# new_list = num_list + numbers
# print(new_list)
# print(numbers[::-2])
# index=num_list.index(20)
# # num_list[index] = 200
# # print(num_list)
#
# for num in num_list:
#     if num == 20:
#         num_list.remove(num)
#
#
# print(num_list)
#
# my_list = ["Hello", "Python"]
# print("-".join(my_list))


# Given two lists create a third list by picking an odd-index element from
# the first list and even index elements from the second.
# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# listThree = []
# for i in range(len(listOne)):
#     if i % 2 == 0:
#         listThree.append(listTwo[i])
#     else:
#         listThree.append(listOne[i])
#
# print(listThree)
#
# # Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
#
# list1 = [34, 54, 67, 89, 11, 43, 94]
# element = list1[4]
# list1.remove(element)
# list1.insert(2,element)
# list1.append(element)
# print(list1)

#
# # Given a list slice it into 3 equal chunks and reverse each chunk
# sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# length = len(sampleList)
# length /= 3
# for i in range(int(length)):
#     slice_obj = slice(int(length * i), int(length * i + length), 1)
#     list_slice = sampleList[slice_obj]
#     print(list_slice)
#     print("reverse :",list(reversed(list_slice)))
#
#  # Iterate a given list and count the occurrence of each element and
# # create a dictionary to show the count of each element
# Original_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# count_dict = {}
# for num in Original_list:
#     count_dict[num] = Original_list.count(num)
# print(count_dict)

# # Given a two list of equal size create a Python set such that it shows the element from both lists in the pair
# First_List = [2, 3, 4, 5, 6, 7, 8]
# Second_List = [4, 9, 16, 25, 36, 49, 64]
# new_set = ()
# new_set = {(x, y) for x, y in zip(First_List, Second_List)}
# print(new_set)

# Given the following two sets find the intersection and remove those elements from the first set
from typing import Set

#
# First_Set = {65, 42, 78, 83, 23, 57, 29}
# Second_Set = {67, 73, 43, 48, 83, 57, 29}
# print("Intersection :", First_Set.intersection(Second_Set))
# print("First set after update: ", First_Set-First_Set.intersection(Second_Set))

# Given two sets, Checks if One Set is a subset or superset of another Set.
# if the subset is found delete all elements from that set
#
# firstSet = {27, 43, 34}
# secondSet = {34, 93, 22, 27, 43, 53, 48}
#
#
# print("firstSet is subset of second set :", firstSet.issubset(secondSet))
# print(" secondSet is subset of first set :", secondSet.issubset(firstSet))
# print("firstSet is superset of second set :", firstSet.issuperset(secondSet))
# print(" secondSet is  superset of first set :", secondSet.issuperset(firstSet))
#
# if firstSet.issubset(secondSet):
#     firstSet.clear()
# else:
#     secondSet.clear()
# print(firstSet)
# print(secondSet)

# Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it
# # from the list
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
for num in rollNumber:
    if num in sampleDict.values():
        continue
    rollNumber.remove(num)
print(rollNumber)



# Given a dictionary get all values from the dictionary and add them to a list but don’t add duplicates
# list1 =[]
# speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
# for val in speed.values():
#     list1.append(val)
#
# list1 = list(set(list1))
# print(list1)
#
# # Remove duplicate from a list and create a tuple and find the minimum and maximum number
# sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
# tuple1 = tuple(set(sampleList))
# print(tuple1)
# print("max", max(tuple1))
# print("min", min(tuple1))
