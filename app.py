import csv

with open("C:/Users/HP/Desktop/quantium-starter-repo-main/quantium-starter-repo-main/data/daily_sales_data_2.csv", mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if(row['product'] == 'pink morsel'):
            Sales = int(row['quantity']) * float(row['price'].replace('$', '').replace(',', ''))
            date = row['date']
            region = row['region']
            print(Sales, date, region)
