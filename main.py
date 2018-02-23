import csv

from row import Row
from collections import defaultdict
import matplotlib.pyplot as plt

PLN = '\ufeffPLN'
TYPE = 'Typ'
PERSON = 'Ponosiciel'
PATH = 'csv_hiszpania.csv'


def read_csv(path):
    rows = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            rows.append(Row(row[PLN], row[TYPE], row[PERSON]))
    return rows


def group_rows_by_type(rows):
    costs = defaultdict(list)
    for row in rows:
        costs[row.type].append(row.pln)
    return costs


def get_type_costs_sum(all_costs):
    sizes = []
    for costs in all_costs:
        sizes.append(sum(float(cost.replace(',', '.')) for cost in costs))
    return sizes


def show_pie_chart(labels, sizes):
    plt.pie(sizes, labels=labels)
    plt.axis('equal')
    plt.show()


def main():
    rows = read_csv(PATH)
    type_costs = group_rows_by_type(rows)
    labels = type_costs.keys()
    sizes = get_type_costs_sum(type_costs.values())
    show_pie_chart(labels, sizes)


if __name__ == '__main__':
    main()
