# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict1 = {key: value for key, value in zip(keys, values)}
# print(dict1)
#
# sampleDict = dict(zip(keys, values))
#
#
# # Merge following two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)
#
# dict3 = {**dict1, **dict2}
# print(dict3)
#
#
# sampleDict = {
#    "class":{
#       "student":{
#          "name":"Mike",
#          "marks":{
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
#
# print(sampleDict['class']['student']['marks']['history'])
# # remove key from dictionary
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# keysToRemove = ["name", "salary"]
# for key in keysToRemove:
#     del sampleDict[key]

# print(sampleDict)


sampleDict = {'a': 100, 'b': 200, 'c': 300}
search = 200
if search in sampleDict.values():
    print(True)

# #change city key to location
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sampleDict['location'] = sampleDict.pop('city')
# print(sampleDict)


sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

print(min(sampleDict.keys()))

empDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

empDict['emp3']['salary'] = 8500

print(empDict)
