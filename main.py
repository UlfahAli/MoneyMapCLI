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

    if remaining >=0:
        print(f"Remaining income after priority outgoings: £{remaining:.2f}")      
    else: 
        shortfall = abs(remaining)
        print("Your income does not cover your priority costs.")
        print(f"Your shortfall is: £{shortfall:.2f}")
        print("This means your essential costs may not be covered this month.")
        print("Consider increasing your income and seeking advice from your local advice centre.")

    
main()