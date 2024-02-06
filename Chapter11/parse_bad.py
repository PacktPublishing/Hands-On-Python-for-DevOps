import csv

with open('MOCK_DATA.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip header if present
        next(csv_reader, None)

        for row in csv_reader:
            print(row)
