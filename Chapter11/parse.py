import csv

def read_large_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip header if present
        next(csv_reader, None)

        for row in csv_reader:
            yield row

# Example usage
csv_file_path = 'MOCK_DATA.csv'
for row in read_large_csv(csv_file_path):
    # Process each row as needed
    print(row)
