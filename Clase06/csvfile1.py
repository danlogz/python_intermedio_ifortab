#Manipular archivos csv

import os

os.system('clar')

with open('console_games.csv','r') as csv_file:
    for line in csv_file.readlines():
        print(line)