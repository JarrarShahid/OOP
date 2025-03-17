# mediator.py

from abc import ABC, abstractmethod


# Step 1: Mediator Interface
class ChatMediator(ABC):
    """Abstract Mediator that facilitates communication between users."""

    @abstractmethod
    def send_message(self, message, user):
        """Broadcast message to all users except the sender."""
        pass

    @abstractmethod
    def add_user(self, user):
        """Register a user to the chatroom."""
        pass


# Step 2: Concrete Mediator
class ChatRoom(ChatMediator):
    """Concrete Mediator that manages communication between users."""

    def __init__(self):
        self.users = []

    def add_user(self, user):
        """Adds a user to the chatroom."""
        self.users.append(user)

    def send_message(self, message, user):
        """Broadcasts a message to all users except the sender."""
        for u in self.users:
            if u != user:
                u.receive_message(message, user.name)


# Step 3: Colleague (User) Class
class User:
    """Represents a user in the chatroom."""

    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    def send_message(self, message):
        """Sends a message through the mediator."""
        print(f"{self.name} 📤: {message}")
        self.mediator.send_message(message, self)

    def receive_message(self, message, sender_name):
        """Receives a message from the chatroom."""
        print(f"{self.name} 📩 received from {sender_name}: {message}")


# Step 4: Demonstration
if __name__ == "__main__":
    print("💬 Setting up chatroom...")
    chatroom = ChatRoom()

    user1 = User("Alice", chatroom)
    user2 = User("Bob", chatroom)
    user3 = User("Charlie", chatroom)

    print("\n🔹 Conversation starts:")
    user1.send_message("Hello, everyone!")
    user2.send_message("Hey Alice, how are you?")
    user3.send_message("Good to see you all here! 😊")
