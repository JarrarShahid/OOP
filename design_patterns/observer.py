from abc import ABC, abstractmethod

# Step 1: Define the Observer interface
class Observer(ABC):
    """Abstract Observer class that defines an update method."""
    
    @abstractmethod
    def update(self, message: str):
        pass

# Step 2: Define the Subject (Observable) class
class Subject:
    """Observable Subject class that maintains a list of observers."""
    
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        """Attach an observer to the subject."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """Detach an observer from the subject."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        """Notify all observers about an event."""
        for observer in self._observers:
            observer.update(message)

# Step 3: Create Concrete Observers
class EmailNotifier(Observer):
    """Observer that simulates sending an email notification."""
    
    def update(self, message: str):
        print(f"[Email Notifier] Received message: {message}")

class SMSNotifier(Observer):
    """Observer that simulates sending an SMS notification."""
    
    def update(self, message: str):
        print(f"[SMS Notifier] Received message: {message}")

class Logger(Observer):
    """Observer that logs messages to a file."""
    
    def update(self, message: str):
        print(f"[Logger] Logging message: {message}")

# Step 4: Demonstration
if __name__ == "__main__":
    subject = Subject()

    # Create Observers
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()
    logger = Logger()

    # Attach observers to the subject
    subject.attach(email_notifier)
    subject.attach(sms_notifier)
    subject.attach(logger)

    # Trigger an event
    subject.notify("A new user has signed up!")

    # Detach one observer and notify again
    subject.detach(sms_notifier)
    subject.notify("User has updated profile settings!")

