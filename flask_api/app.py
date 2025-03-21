# app.py

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from models import db
from routes import UserResource, PostResource

# Initialize Flask App
app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # Change to PostgreSQL/MySQL if needed
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)
api = Api(app)

# Register API Endpoints
api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(PostResource, "/posts", "/posts/<int:post_id>")

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Database Initialization
@app.before_first_request
def create_tables():
    db.create_all()

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

