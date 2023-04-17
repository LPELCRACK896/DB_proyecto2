from hbase import Master
from data_generator import gen_games, gen_purchase
def main():
    # gen_purchase("purchases.json", 1)
    # gen_games("games.json", 2)
    hbase = Master()
    hbase.load_data_from_json("Sales", "./back/purchases.json")
    hbase.load_data_from_json("Games", "./back/games.json")
    print("---Sales---")
    print(hbase.scan("Sales")[1])
    print("\t\t")
    print("---Games---")
    print(hbase.scan("Games")[1])
    games_count = hbase.count("Games")
    print(f"Count: {games_count[1]}")
    print(hbase.truncate("Games"))
    print("---Games after truncate---")
    print(hbase.scan("Games")[1])
    games_count = hbase.count("Games")
    print(f"Count: {games_count[1]}")
    # Create a table
    """ 
    status, message = hbase.create_table("Sales", ["customer_info", "purchase_info", "product_info"])
    print(f"Create table: {status}, {message}")

    # Insert data
    hbase.put("Sales", "7512", "customer_info", "Name", "Jeremy Garcia")
    hbase.put("Sales", "7512", "customer_info", "Age", 26)
    hbase.put("Sales", "7512", "customer_info", "Address", "545 Mcpherson Fords\nKatherinetown, MP 35670")
    hbase.put("Sales", "7512", "purchase_info", "Date", "2022-04-25")
    hbase.put("Sales", "7512", "purchase_info", "Time", "01:14:49")
    hbase.put("Sales", "7512", "purchase_info", "Total Price", 79.28)
    hbase.put("Sales", "7512", "purchase_info", "Payment Type", "Debit Card")
    hbase.put("Sales", "7512", "product_info", "Product ID", 2195)
    hbase.put("Sales", "7512", "product_info", "Product Name", "fill")
    hbase.put("Sales", "7512", "product_info", "Quantity", 9)

    status, data = hbase.get("Sales", "7512", "customer_info", "Name")
    print(f"Get data: {status}, {data}")

    hbase.put("Sales", "7512", "customer_info", "Name", "Jeremy G. Updated")
    status, data = hbase.get("Sales", "7512", "customer_info", "Name")
    print(f"Get updated data: {status}, {data}")

    status, message = hbase.disable("Sales")
    print(f"Disable table: {status}, {message}")

    status, message = hbase.put("Sales", "7512", "customer_info", "Name", "Disabled Table Update")
    print(f"Put data in disabled table: {status}, {message}")

    status, message = hbase.enable("Sales")
    print(f"Enable table: {status}, {message}")

    #hbase.put("Sales", "7512", "customer_info", "Name", "Jeremy G. Enabled")
    status, data = hbase.get("Sales", "7512", "customer_info", "Name")
    print(f"Get updated data after enabling table: {status}, {data}") """

if __name__ == "__main__":
    main()
