import csv


def get_transaction_data(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents         

def main():
    with open("data/transactions.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        total_priority = 0
        for row in readCSV:
            amount = float(row[2])
            type_ = row[3]
            if type_ == "Priority" or type_ == "Essential":
                total_priority += amount

    income = float(input("What is your monthly income?"))
    remaining = income - total_priority 

    print(f"Total priority costs: £{total_priority}")        
    print(f"Remaining income after priority outgoings: £{remaining}")
    
main()