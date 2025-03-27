import json

# with open("data.json") as file:
#     data = json.load(file)

# new_data = []

# for datum in data:
#     new_datum = []
#     for string in datum:
#         try:
#             new_string = string.strip()
#             new_string = new_string.encode("ascii", "ignore").decode()
#             new_datum.append(new_string)
#         except:
#             new_datum.append(string)
    
#     new_data.append(new_datum)

# with open("ss.json", 'w') as json_file:
#     json.dump(new_data, json_file, indent=4)

import csv

header = ['No', 'Website', 'Price', 'Country', 'Language', 'Industry', 'Duration']

# data = [
#     ['Afghanistan', 652090, 'AF', 'AFG'],
#     ['Albania', 28748, 'AL', 'ALB'],
#     ['Algeria', 2381741, 'DZ', 'DZA']
# ]

data = []

with open("ss.json") as file:
    i_data = json.load(file)

for index, i_datum in enumerate(i_data):
    try:
        data.append([index+1, i_datum[0], i_datum[1], i_datum[3], i_datum[4], i_datum[6], i_datum[7]])
    except:
        pass
with open('countries.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    writer.writerows(data)
            
        
        