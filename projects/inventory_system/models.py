from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    sales = relationship("Sale", back_populates="product")

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity_sold = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    product = relationship("Product", back_populates="sales")
