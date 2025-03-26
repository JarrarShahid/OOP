from storage import Database
from inventory_manager import InventoryManager

def main():
    db = Database()
    manager = InventoryManager(db)

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. View Products")
        print("4. View Sales")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            manager.add_product(name, quantity, price)

        elif choice == "2":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity to sell: "))
            manager.sell_product(name, quantity)

        elif choice == "3":
            manager.list_products()

        elif choice == "4":
            manager.list_sales()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
