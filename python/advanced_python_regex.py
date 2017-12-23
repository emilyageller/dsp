"""
Regular Expressions, Dictionary, Writing to CSV File
This question has multiple parts, and will take 20+ hours to complete, depending on your python proficiency level. Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp. Note: Do not use Pandas library to complete this section.

For Part 1, use of regular expressions is optional.
"""
# Part I - Regular Expressions

# Q1: Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
# Solution:
import csv
import re


def count_degrees(csv_file_name):
    with open(csv_file_name, 'r') as f:
        data = [row for row in csv.reader(f)]
    degrees = []
    for row in data:
        degrees.append(row[1])
    for i in range(len(degrees)):
        degrees[i] = degrees[i].split()
    for i in range(len(degrees)):
        for j in range(len(degrees[i])):
            degrees[i][j] = re.sub(r" ?Ph.?D.?", r"PhD", degrees[i][j])
            degrees[i][j] = re.sub(r" ?Sc.?D.?", r"ScD", degrees[i][j])
            degrees[i][j] = re.sub(r" ?M.?S.?", r"MS", degrees[i][j])
            degrees[i][j] = re.sub(r" ?B.?S.?Ed.?", r"BSED", degrees[i][j])
    degreedict = {}
    for i in range(1, len(degrees)):
        for j in range(len(degrees[i])):
            if degrees[i][j] in degreedict:
                degreedict[degrees[i][j]] += 1
            else:
                degreedict[degrees[i][j]] = 1
    return degreedict

#Q2: Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
    # Solution

    def count_titles(csv_file_name):
        with open(csv_file_name, 'r') as f:
            data = [row for row in csv.reader(f)]
        titles = []
        for row in data:
            titles.append(row[2])
        for i in range(len(titles)):
            titles[i] = re.sub(r"^Associate.+", r"associate", titles[i])
            titles[i] = re.sub(r"^Professor.+", r"professor", titles[i])
            titles[i] = re.sub(r"^Assistant.+", r"assistant", titles[i])
        titledict = {}
        for i in range(1, len(titles)):
            if titles[i] in titledict:
                titledict[titles[i]] += 1
            else:
                titledict[titles[i]] = 1
        return titledict

# Q3. Search for email addresses and put them in a list. Print the list of email addresses.
# Solution:

def emails(csv_file_name):
    with open(csv_file_name, 'r') as f:
        data = [row for row in csv.reader(f)]
    emails = []
    for i in range(1,len(data)):
        emails.append(data[i][3])
    
    return emails

# Q4: Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

def unique_domains(emails):
    domains = []
    unique_domains = {}
    for i in range(len(emails)):
        match = re.search(r'@.+', emails[i])
        domains.append(match.group(0)[1:])
    for i in range(len(domains)):
        if domains[i] in unique_domains:
            unique_domains[domains[i]] += 1
        else:
            unique_domains[domains[i]] = 1
    return unique_domains

    
