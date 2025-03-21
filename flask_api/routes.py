# routes.py

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models import db, User, Post

app = Flask(__name__)
api = Api(app)

# API Resource for Users
class UserResource(Resource):
    def get(self, user_id=None):
        """Get a specific user by ID or return all users"""
        if user_id:
            user = User.query.get(user_id)
            if user:
                return jsonify({
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "created_at": user.created_at
                })
            return {"message": "User not found"}, 404
        users = User.query.all()
        return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])

    def post(self):
        """Create a new user"""
        data = request.get_json()
        new_user = User(username=data["username"], email=data["email"], password_hash=data["password"])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created", "id": new_user.id}, 201

    def put(self, user_id):
        """Update user details"""
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        data = request.get_json()
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        db.session.commit()
        return {"message": "User updated"}

    def delete(self, user_id):
        """Delete a user"""
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}

# API Resource for Posts
class PostResource(Resource):
    def get(self, post_id=None):
        """Get a specific post by ID or return all posts"""
        if post_id:
            post = Post.query.get(post_id)
            if post:
                return jsonify({
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                    "created_at": post.created_at,
                    "user_id": post.user_id
                })
            return {"message": "Post not found"}, 404
        posts = Post.query.all()
        return jsonify([{"id": p.id, "title": p.title, "content": p.content, "user_id": p.user_id} for p in posts])

    def post(self):
        """Create a new post"""
        data = request.get_json()
        new_post = Post(title=data["title"], content=data["content"], user_id=data["user_id"])
        db.session.add(new_post)
        db.session.commit()
        return {"message": "Post created", "id": new_post.id}, 201

    def put(self, post_id):
        """Update post details"""
        post = Post.query.get(post_id)
        if not post:
            return {"message": "Post not found"}, 404
        data = request.get_json()
        post.title = data.get("title", post.title)
        post.content = data.get("content", post.content)
        db.session.commit()
        return {"message": "Post updated"}

    def delete(self, post_id):
        """Delete a post"""
        post = Post.query.get(post_id)
        if not post:
            return {"message": "Post not found"}, 404
        db.session.delete(post)
        db.session.commit()
        return {"message": "Post deleted"}

# Register API Endpoints
api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(PostResource, "/posts", "/posts/<int:post_id>")

if __name__ == "__main__":
    app.run(debug=True)
