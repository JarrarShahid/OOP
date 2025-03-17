# mvc_pattern.py

class UserModel:
    """Model: Handles user data."""
    
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, email):
        """Adds a new user to the database."""
        self.users[user_id] = {"name": name, "email": email}

    def get_user(self, user_id):
        """Retrieves user information."""
        return self.users.get(user_id, None)

    def delete_user(self, user_id):
        """Deletes a user from the database."""
        if user_id in self.users:
            del self.users[user_id]

    def get_all_users(self):
        """Returns all users."""
        return self.users


class UserView:
    """View: Handles UI logic (printing data)."""

    @staticmethod
    def show_user_details(user):
        """Displays user details."""
        if user:
            print(f"👤 User: {user['name']} | 📧 Email: {user['email']}")
        else:
            print("❌ User not found!")

    @staticmethod
    def show_all_users(users):
        """Displays all users in the system."""
        if users:
            print("\n📜 User List:")
            for user_id, user in users.items():
                print(f"🔹 ID: {user_id} | {user['name']} | {user['email']}")
        else:
            print("🚫 No users available.")


class UserController:
    """Controller: Connects Model and View."""

    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

    def add_user(self, user_id, name, email):
        """Handles adding a user."""
        self.model.add_user(user_id, name, email)
        print(f"✅ User '{name}' added successfully!")

    def show_user(self, user_id):
        """Handles fetching and displaying user details."""
        user = self.model.get_user(user_id)
        self.view.show_user_details(user)

    def show_all_users(self):
        """Handles displaying all users."""
        users = self.model.get_all_users()
        self.view.show_all_users(users)

    def delete_user(self, user_id):
        """Handles deleting a user."""
        self.model.delete_user(user_id)
        print(f"🗑️ User with ID '{user_id}' deleted.")


# Step 4: Demonstration
if __name__ == "__main__":
    controller = UserController()

    # Adding users
    controller.add_user(1, "Alice", "alice@example.com")
    controller.add_user(2, "Bob", "bob@example.com")

    # Displaying users
    print("\n🔍 Fetching Users:")
    controller.show_user(1)
    controller.show_user(3)  # Non-existing user

    # Displaying all users
    controller.show_all_users()

    # Deleting a user
    controller.delete_user(1)
    
    # Display updated users
    controller.show_all_users()

