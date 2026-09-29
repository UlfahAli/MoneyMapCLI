def get_transaction_data(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents         

def main():
    file_contents = get_transaction_data("data/transactions.csv")
    print(file_contents)

main()