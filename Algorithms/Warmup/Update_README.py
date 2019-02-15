import json

with open('readme.json') as f:
    data = json.load(f)

solution_base_url = "https://github.com/barone-dev/HackerRank/blob/master/"
solution_base_url += data['domain'] + "/" + data['subdomain'] + "/"

title = "# " + data['subdomain']
table_header = "| " + " | ".join(data['headers']) + " |"
table_config = "|:---:|:--- |:---:|:---:|"
table_content = {}

for difficulty in sorted(data['solutions'].keys()):
    dif_dict = data['solutions'][difficulty]
    difficulty = difficulty[2:]
    print("-----------" + difficulty + "-----------")
    for i in range(len(dif_dict)):
        table_item = "| " + difficulty + " | "
        table_item += "[" + dif_dict[i]['challenge']['title'] + "]"
        table_item += "(" + dif_dict[i]['challenge']['url'] + ") | "
        table_item += str(dif_dict[i]['points']) + " | "
        table_item += "[" + dif_dict[i]['solution']['title'] + "]"
        file_url = solution_base_url + dif_dict[i]['solution']['filename']
        table_item += "(" + file_url + ") |"

        table_content[dif_dict[i]['challenge']['title']] = table_item
        print(table_item)

lines = [title, table_header, table_config]
for k in sorted(table_content):
    lines.append(table_content[k])

with open('README.md', 'w') as file:
    for line in lines:
        file.write(line + '\n')
