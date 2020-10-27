import json
# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
    print(data['1'])

    # for printing the key-value pair of
    # nested dictionary for looop can be used
    # print("\nPrinting nested dicitonary as a key-value pair\n")
    # for i in data['people1']:
    #     print("Name:", i['name'])
    #     print("Website:", i['website'])
    #     print("From:", i['from'])
    #     print()
