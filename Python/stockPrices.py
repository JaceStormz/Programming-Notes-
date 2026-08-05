# 08/06/2026
# stockPrices.py

def operation(dictionary):

    table = input("Pick a Table info, ril or mtl?: ").strip().lower()
    logic = input("Pick Operator Avg Total Query?: ").strip().lower()

    if table in dictionary:
        records = dictionary[table]

        if logic == "avg":            
            average = sum(records) / len(records)
            print(average)

        elif logic == "total":
            total = sum(records)
            print(total)

        elif logic == "query":
            print(records)

        else:
            print("Invalid Operation.")

    else:
        print("Record not found.")

    

stock = {
    "info":[600, 630, 620],
    "ril":[ 1430, 1490, 1567],
    "mtl":[234, 180, 160]
}


operation(stock)

    
