import csv
from pprint import pprint


def read_csv(station_file):
    with open(station_file, encoding='utf-8', newline='') as csv_file:
    #fieldnames = ('Name', 'Street', 'District')
        reader = csv.DictReader(csv_file)
        list_station = [dict(row) for row in reader]
    return list_station


station_list = read_csv('data-398-2018-08-30.csv')
pprint(station_list)