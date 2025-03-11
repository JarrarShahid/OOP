import sys
from basics.encapsulation import EncapsulationExample
from basics.inheritance import InheritanceExample
from basics.polymorphism import PolymorphismExample
from basics.abstraction import AbstractionExample

def show_menu():
    print("\nPython OOP Showcase")
    print("1. Encapsulation")
    print("2. Inheritance")
    print("3. Polymorphism")
    print("4. Abstraction")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            obj = EncapsulationExample()
            obj.demo()
        elif choice == "2":
            obj = InheritanceExample()
            obj.demo()
        elif choice == "3":
            obj = PolymorphismExample()
            obj.demo()
        elif choice == "4":
            obj = AbstractionExample()
            obj.demo()
        elif choice == "5":
            print("Exiting...\n")
            sys.exit()
        else:
            print("Invalid choice! Please select again.")

if __name__ == "__main__":
    main()


