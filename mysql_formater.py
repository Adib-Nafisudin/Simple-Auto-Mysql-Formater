from tkinter import filedialog as fdialog

filedata = fdialog.askopenfilename()

with open(filedata) as file:
    data_list = file.readlines()

print("\nInput table name")
table_name = input()
data = (f"DROP TABLE IF EXISTS `{table_name}`;\n")

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return "NULL"
    if reply[0] == 'n':
        return "NOT NULL"
    else:
        return yes_or_no("please enter y/n")

def primary_key_choice(table_data):
    print("Select Primary Key")
    count = 0
    for data in table_data:
        count += 1
        print(f"{count}: {data}")
    z = int(input())
    z -= 1
    return z

def table_creation_format(table_data):
    
    table_insert_data = []
    for data in table_data:
        data = data.strip()
        data = (f"`{data}`")
        table_insert_data.append(data)

    column_name = (', '.join(table_insert_data))
    
    table_element = (f"CREATE TABLE `{table_name}` (\n")
    for column_data in table_data:
        print(f"\nInput data type for {column_data.strip()}:")
        data_type = input()
        print(f"\nInput length/values {column_data.strip()}:")
        length = input()
        null = yes_or_no("\nnull or not null")
        element = (f'\t`{column_data.strip()}` {data_type}({length}) {null},\n')
        table_element = table_element + element
    
    y = primary_key_choice(table_insert_data)
    table_element += (f"\tPRIMARY KEY (`{table_data[y]}`));\n\nINSERT INTO `{table_name}` ({column_name})\nVALUES\n")
    
    # print(table_element)
    return table_element

formater = ""
count = 0
for data_string in data_list:
    count += 1
    data_string = data_string.replace("\""," ")
    data_string = data_string.replace("\'"," ")
    line_list = data_string.split(',')
    if count == 1:
        table_format = table_creation_format(line_list)
        data += table_format
    else:
        if count == len(data_list):
            tail = ";"
        else:
            tail = ","
        formater = (f'\t(\"{line_list[0]}\",\"{line_list[1]}\",\"{line_list[2]}\",\"{line_list[3]}\",\"{line_list[4].strip()}\"){tail}\n')
        data += formater
        
final_data = data
# print(final_data)

with open('mysql_formater.sql','w') as writefile:
    writefile.write(final_data)