from pprint import  pprint
import os
path = os.getcwd()
ls = [file for file in os.listdir(path) if file.endswith(".txt")]


ls_1 = []
for file in ls:
    with open(file) as f:
        text = f.readlines()
        line_count = 0
        for line in text:
            line_count += 1
        ls_1.append([line_count, file, text])
ls_1.sort()

with open('final.txt', 'w') as f:
    for item in ls_1:
        f.write(f'{item[1]} \n')
        f.write(f'{item[0]} \n')
        for line in item[2]:
            f.write(line)




