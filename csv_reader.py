import csv
with open('/Users/nate/Desktop/surveys.csv', 'rb') as fil:
    reader = csv.reader(fil)
    for row in reader:
        print row
