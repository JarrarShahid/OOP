# models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base
from pydantic import BaseModel

# SQLAlchemy Model (Database Representation)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    posts = relationship("Post", back_populates="author", cascade="all, delete")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    author = relationship("User", back_populates="posts")

# Pydantic Models (Request/Response Validation)
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass  # Used for user creation

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Allows SQLAlchemy conversion

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int

class PostResponse(PostBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
