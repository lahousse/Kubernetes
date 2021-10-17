import yaml

dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open(r'file_location', 'w') as file:
    documents = yaml.dump(dict_file, file)