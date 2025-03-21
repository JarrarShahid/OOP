# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model representing a registered user"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship: One User -> Many Posts
    posts = db.relationship("Post", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    """Post model representing a user's post"""
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key to associate Post with a User
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationship: Each post is linked to a single user
    author = db.relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post {self.title} by User {self.user_id}>"
