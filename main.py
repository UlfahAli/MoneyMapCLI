import csv


def get_transaction_data(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents         

def main():
    with open("data/transactions.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)

main()