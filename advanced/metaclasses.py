# metaclasses.py

class AttributeNamingMeta(type):
    """
    A metaclass that enforces attribute naming conventions in class creation.
    Attributes must be in lowercase with underscores.
    """

    def __new__(cls, name, bases, class_dict):
        for attr_name in class_dict:
            if not attr_name.startswith("__") and not attr_name.islower():
                raise TypeError(f"Attribute '{attr_name}' in class '{name}' must be lowercase with underscores.")
        return super().__new__(cls, name, bases, class_dict)


# Example usage of metaclass
class User(metaclass=AttributeNamingMeta):
    first_name = "John"
    last_name = "Doe"
    email_address = "john.doe@example.com"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# Uncommenting the following class will raise an error due to naming violations
"""
class InvalidUser(metaclass=AttributeNamingMeta):
    FirstName = "Alice"  # This will raise TypeError
    LastName = "Smith"    # This will also raise TypeError
"""

if __name__ == "__main__":
    user = User()
    print(user.get_full_name())

    # The following line will cause an error if you uncomment the InvalidUser class
    # invalid_user = InvalidUser()
