__author__ = 'animesh'
import csv


def parse_csv(path_to_csv):
    csv_file = open(path_to_csv, 'rb')
    reader = csv.reader(csv_file, delimiter='\t')
    precipitation_details = {}
    for row in reader:  # iterates the rows of the file in orders
        if len(row) < 1:  # remove first row from csv file
            continue
        if row[0].isalpha():  # remove second row from csv file
            continue
        year = row[0]
        del row[0]
        precipitation_details[year] = row
    return precipitation_details


def get_monthly_data(precipitation, start_year, end_year, month):
    monthly_data = []
    for year in range(start_year, end_year):
        monthly_data.append(precipitation[str(year)][month])
    return monthly_data