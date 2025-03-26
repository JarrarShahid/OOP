# Inventory Management System (OOP & SQLite)

## 📌 Overview
This project is an **Object-Oriented Python-based Inventory Management System** using **SQLite** and **SQLAlchemy**.  
It allows users to:
- **Add new products** to the inventory.
- **Sell products**, reducing stock.
- **View available products** in stock.
- **Track sales transactions** with timestamps.

## 🚀 Features
✅ Add products with name, quantity, and price  
✅ Sell products and update stock automatically  
✅ View product inventory and stock levels  
✅ Track sales history with total price and date  
✅ Data persistence using **SQLite database**  

## 📂 Project Structure
```sh
inventory_system/ 
│── main.py # Entry point for the inventory system 
│── models.py # Defines Product, Sale, and related models 
│── inventory_manager.py # Business logic for managing inventory 
│── cli.py # Command-line interface for inventory operations 
│── storage.py # Handles database interactions (SQLite) 
│── requirements.txt # List of dependencies 
│── README.md # Documentation for the project
```


## 🛠️ Installation
1. **Clone the repository**
```bash
git clone https://github.com/your-repo/OOP-Python-Showcase.git
cd OOP-Python-Showcase/projects/inventory_system
```
2. **Create a virtual environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
## ▶️ Running the Project
```python main.py```

## 🖥️ Usage (CLI Options)

1️⃣ Add Product

```sh
Enter product name: Laptop
Enter quantity: 5
Enter price: 1000
Product 'Laptop' added/updated successfully.
```

2️⃣ Sell Product

```sh
Enter product name: Laptop
Enter quantity to sell: 2
Sold 2 of 'Laptop' for $2000.
```

3️⃣ View Products

```sh
1: Laptop - 3 in stock - $1000 each
```

4️⃣ View Sales

```sh
Sale ID: 1 - Product: Laptop - Quantity: 2 - Total: $2000 - Date: 2024-03-25 12:00:00
```

5️⃣ Exit Application

```sh
Exiting...
```