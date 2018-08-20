import json
# from pprint import pprint
# import pygeoj


# with open('wits-buildings.json') as f:
#     data = json.loads(f)


# with open('wits-buildings.js') as f:
#     data = json.loads(f.read())
#     print(data['features'][0]["id"])

f = open("wits.txt","r")
stringVar = f.read()
f.close()
stringVar = stringVar.replace("var gara = {", "{")
# print(stringVar)

data = json.loads(stringVar)
# print(data['features'][0]["id"] )
data['features'][0]["id"] = "05"

# print(data['features'][0]["id"] )

stringVar = "var gara = " + json.dumps(data)
print(stringVar)


f = open("wits.txt","w")
f.write(stringVar)
f.close()

# pprint(data)

# with open('wits.txt', 'w') as outfile:  
#     json.dump(data, outfile)

# testfile = pygeoj.load(filepath="wits-buildings.json")
# testfile = pygeoj.load(data)

# print(len(testfile))