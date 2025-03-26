from models import Product, Sale
from storage import Database

class InventoryManager:
    def __init__(self, db: Database):
        self.db = db

    def add_product(self, name, quantity, price):
        session = self.db.get_session()
        try:
            product = session.query(Product).filter_by(name=name).first()
            if product:
                product.quantity += quantity
            else:
                product = Product(name=name, quantity=quantity, price=price)
                session.add(product)
            session.commit()
            print(f"Product '{name}' added/updated successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error adding product: {e}")
        finally:
            session.close()

    def sell_product(self, name, quantity):
        session = self.db.get_session()
        try:
            product = session.query(Product).filter_by(name=name).first()
            if not product or product.quantity < quantity:
                print("Insufficient stock or product not found.")
                return
            
            total_price = product.price * quantity
            product.quantity -= quantity
            sale = Sale(product=product, quantity_sold=quantity, total_price=total_price)
            session.add(sale)
            session.commit()
            print(f"Sold {quantity} of '{name}' for ${total_price}.")
        except Exception as e:
            session.rollback()
            print(f"Error processing sale: {e}")
        finally:
            session.close()

    def list_products(self):
        session = self.db.get_session()
        try:
            products = session.query(Product).all()
            for product in products:
                print(f"{product.id}: {product.name} - {product.quantity} in stock - ${product.price} each")
        except Exception as e:
            print(f"Error fetching products: {e}")
        finally:
            session.close()

    def list_sales(self):
        session = self.db.get_session()
        try:
            sales = session.query(Sale).all()
            for sale in sales:
                print(f"Sale ID: {sale.id} - Product: {sale.product.name} - Quantity: {sale.quantity_sold} - Total: ${sale.total_price} - Date: {sale.date}")
        except Exception as e:
            print(f"Error fetching sales: {e}")
        finally:
            session.close()
