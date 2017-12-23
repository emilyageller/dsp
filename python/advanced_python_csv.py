# Part II - Write to CSV File
# Q5. Write email addresses from Part I to csv file

fout = open('emails.csv', 'w')
e = emails(f'faculty.csv')
for i in range(len(e)):
    fout.write(e[i])
    fout.write('\n')
fout.close()