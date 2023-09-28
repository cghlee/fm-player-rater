#! python3

# player_rater.py - Generates weighted ratings for Football Manager players
# provided in CSV format according to attribute testing performed by FM-Arena

import os, csv

# Initialise attribute weightings according to tests performed by FM-Arena
attrib_weight = {'Dri': 1/5, 'Fin': 6/25, 'Fir': 2/25, 'Lon': 2/25,
                 'Mar': 2/25, 'Pas': 4/25, 'Tck': 1/25, 'Tec': 1/25,
                 'Ant': 8/25, 'Cmp': 1/25, 'Cnt': 6/25, 'Dec': 2/25,
                 'OtB': 1/25, 'Tea': 1/25, 'Vis': 3/25, 'Wor': 1/5,
                 'Acc': 4/5, 'Agi': 7/25, 'Bal': 7/25, 'Jum': 2/5,
                 'Pac': 1, 'Sta': 4/25, 'Str': 4/25}

# Use 'players.csv' path by default, else use user input for CSV file location
for path in os.listdir():
    if path.lower() == 'players.csv':
        csv_path = 'players.csv'
        break
else:
    csv_path = input("Please input name of CSV file containing player data:\n")
    if not csv_path.lower().endswith('.csv'):
        csv_path = csv_path + '.csv'

# Break out of program if path for CSV does not exist
if csv_path not in os.listdir():
    print('CSV file not found.\nPlease restart program and try again.')
    quit()

# Store index information for player attributes and name data
with open(csv_path, encoding='utf-8') as file:
    csv_file = csv.reader(file)
    attrib_index = {}
    for line in csv_file:
        if 'Transfer Status' in line:
            for key in attrib_weight:
                attrib_index[key] = line.index(key)
            name_index = line.index('Name')
            break
    file.close()

# Generate weighted ratings for each player listed in the provided CSV file
with open(csv_path, encoding='utf-8') as file:
    players = {}
    csv_file = csv.reader(file)
    for line in csv_file:
        total_curr = 0
        if 'Transfer Status' in line:
            continue
        if line[name_index]:
            for key, value in attrib_index.items():
                attrib_curr = attrib_weight[key] * int(line[value])
                total_curr += attrib_curr
            players[line[name_index]] = float(f'{total_curr:.2f}')
    file.close()

# Sort and print weighted ratings for players listed in the provided CSV file
players = sorted(players.items(), key=lambda x: x[1], reverse=True)
print('Weighted Player Ratings:')
for key, value in players:
    print(' - %s (%s)' % (key, value))