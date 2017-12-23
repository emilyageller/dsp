
# Part III - Dictionary

import csv
import re

# Q6. Create a dictionary in the below format:
def get_list():
    f = open('faculty.csv', 'r')
    reader = csv.reader(f)
    faculty_list = [row for row in reader]
    return faculty_list


def get_dict():
    faculty_list =  get_list()
    #faculty_list = faculty_list[1:]
    last_name = []
    for i in range(len(faculty_list)):
        match = re.search(r'[A-Za-z]+$', faculty_list[i][0])
        last_name.append(match.group(0))
    #last_name = last_name[1:]
    my_dict = {}
    for i in range(len(last_name)):
        if last_name[i] in my_dict:
            my_dict[last_name[i]].append(faculty_list[i][1:])
        else:
            my_dict[last_name[i]] = [faculty_list[i][1:]]
    return my_dict

#Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:

#a: Hackerrank version
def get_dict2():
    faculty_list =  get_list()
    #faculty_list = faculty_list[1:]
    my_dict = {}
    for i in range(1, len(faculty_list)):
        match = re.search(r'([\S]+) *([\S]*) ([\S]+)', faculty_list[i][0])
        if match.group(2) == '':
            my_dict[match.group(1), match.group(3)] = faculty_list[i][1:]
        else:
            my_dict[match.group(1), match.group(2), match.group(3)] = faculty_list[i][1:]
    return my_dict

#b: succinct version:
def get_dict2():
    faculty_list =  get_list()
    #faculty_list = faculty_list[1:]
    my_dict = {}
    for i in range(1, len(faculty_list)):
        match = re.search(r'([\S]+) *([\S]*) ([\S]+)', faculty_list[i][0])
        my_dict[match.group(1), match.group(2), match.group(3)] = faculty_list[i][1:]
    return my_dict

# Q8: Alphabetize by last name:

def get_dict3():
    faculty_list =  get_list()
    my_dict = {}
    for i in range(1, len(faculty_list)):
        match = re.search(r'([\S]+) *([\S]*) ([\S]+)', faculty_list[i][0])
        my_dict[match.group(1), match.group(2), match.group(3)] = faculty_list[i][1:]
    return my_dict

answer3 = get_dict3()

keys_sorted = sorted(answer3, key = lambda key: key[2])
# list_sorted = [] option 2
for i in range(len(answer3)):
    # list_sorted.append([keys_sorted[i], answer3[keys_sorted[i]]]) option 2
    print(keys_sorted[i], answer3[keys_sorted[i]])
