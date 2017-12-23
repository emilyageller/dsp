# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

"""
With Pandas:
import pandas as pd
data = pd.read_csv('football.csv')
diff = []
diff = abs(data['Goals'] - data['Goals Allowed'])
print(data['Team'].iloc[diff.idxmin()])
"""

# Without Pandas:

import csv


def read_data(filename):
    with open(filename, 'r') as f:
        data = [row for row in csv.reader(f)]
    return data


def get_index_with_min_abs_score_difference(goals):
    diff = []
    for i in range(1, len(goals)):
        d = int(goals[i][5]) - int(goals[i][6])
        diff.append(abs(d))
    m_index = diff.index(min(diff)) + 1
    return m_index


def get_team(index_value, parsed_data):
    return parsed_data[index_value][0]


# Application:
footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))
