import json
jsonObject = json.load(open('sample.json'))

ratings = list()

for i in jsonObject:
    ratings.append(jsonObject[i])

print(ratings[0]['Content'])