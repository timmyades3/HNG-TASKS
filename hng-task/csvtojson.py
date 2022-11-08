import csv
import json

csv_file_path = input(r'Enter the path to your csv file > ')
# example C:\Users\oluwa\Desktop\MY PROJECTS\HNG TASKS\hng-task\NFT Naming csv - Team Clutch (1).csv
json_file_path = input(r'Enter the path where you want the json file to be located > ')
# example C:\Users\oluwa\Desktop\MY PROJECTS\HNG TASKS\hng-task\Team Clutch json
csv_file = open(csv_file_path, 'r')
csv_reader = csv.DictReader(csv_file)
data = {}
j_format = 'CHIP-0007'

for row in csv_reader:
    out = json.dumps(row, indent=4)
    a = json.loads(out)
    data['format'] = j_format
    data['name'] = str(a['Filename'])
    data['description'] = str(a['Description'])
    data['minning_tool'] = ""
    data['sensitive_content'] = False
    data['series_number'] = int(a['Serial Number'])
    data['series_total'] = 380
    data['atrributes'] = [
        {
            'trait_type': 'gender',
            'value': str(a['Gender'])
        }
    ]
    data['collection'] = {
        'id': 'b774f676-c1d5-422e-beed-00ef5510c64d',
        'name': 'Zuri NFT Tickets for Free Lunch',
        'attribute': [
            {
                'type': 'description',
                'value': 'Reward for accomplishment during HNG9'

            }
        ]}
    data['data'] = [
        {
            'uuid': str(a['UUID']),
            'hash': str(a['HASH'])
        }
    ]

    jsonoutput = open(json_file_path+'\\'+str(a['Filename'])+'.json', 'w')
    jsonoutput.write(json.dumps(data, indent=6))


jsonoutput.close()
csv_file.close()
