import csv

for file_path in [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv"
]:
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)                
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if(row['product'] == 'pink morsel'):
            Sales = int(row['quantity']) * float(row['price'].replace('$', '').replace(',', ''))
            date = row['date']
            region = row['region']
            print(Sales, date, region)
