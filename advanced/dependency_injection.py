# dependency_injection.py

class Logger:
    """A simple Logger class to log messages."""
    
    def log(self, message):
        print(f"[LOG]: {message}")


class FileLogger(Logger):
    """A logger that writes logs to a file."""
    
    def __init__(self, filename="app.log"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as file:
            file.write(f"[LOG]: {message}\n")
        print(f"Logged to file: {message}")


class Application:
    """Application class demonstrating dependency injection."""

    def __init__(self, logger: Logger):
        """Inject a logger dependency via the constructor."""
        self.logger = logger

    def run(self):
        """Simulate running the application."""
        self.logger.log("Application has started.")
        self.logger.log("Performing some tasks...")
        self.logger.log("Application is shutting down.")


# Example Usage
if __name__ == "__main__":
    console_logger = Logger()  # Injecting a Console Logger
    app1 = Application(console_logger)
    app1.run()

    print("\nSwitching to FileLogger...\n")

    file_logger = FileLogger()  # Injecting a File Logger
    app2 = Application(file_logger)
    app2.run()
