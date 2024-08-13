import csv
# Writing data to CSV file
with open('C:\\Users\\god\\Desktop\\Kausik\\Kausik yt\\alpha\\alpha1.csv', 'w', newline='') as
csvfile:
spamwriter = csv.writer(csvfile, delimiter=' ',

quotechar='|', quoting=csv.QUOTE_MINIMAL)

spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
# Reading the tenth row from CSV file
with open('C:\\Users\\god\\Desktop\\Kausik\\Kausik yt\\alpha\\alpha1.csv', 'r') as csvfile:
spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# Skip the first 9 rows
for _ in range(9):
next(spamreader)
# Reading the tenth row
tenth_row = next(spamreader)
print(', '.join(tenth_row))
