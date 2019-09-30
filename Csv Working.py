# Create a text file named grades.csv
#Write to it
#1,Red,A
#2,Green,B
#3,White,A
#Then read it wtih the column names "ID","Name","Grade"

import csv
with open('grades.csv',mode='w',newline='') as grades:
    writer = csv.writer(grades)
    writer.writerow([1,'Red','A'])
    writer.writerow([2, 'Green', 'B'])
    writer.writerow([3, 'White', 'A'])

with open('grades.csv',mode='r',newline='') as grades:
    print(f"{'ID':<4}{'Name':<7}{'Grade'}")
    reader = csv.reader(grades)
    for record in reader:
        stud_no, name, grade = record
        print(f'{stud_no:<4}{name:<7}{grade}')
