from abc import ABC, abstractmethod

# Abstraction: High-level module depends on an interface, not a concrete class
class ILogger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Low-level module: Implements the ILogger interface
class ConsoleLogger(ILogger):
    def log(self, message: str):
        print(f"[Console Log]: {message}")

class FileLogger(ILogger):
    def log(self, message: str):
        with open("log.txt", "a") as file:
            file.write(f"[File Log]: {message}\n")

# High-level module: Depends on the ILogger interface, not a specific logger
class PaymentProcessor:
    def __init__(self, logger: ILogger):
        self.logger = logger

    def process_payment(self, amount: float):
        # Payment logic...
        self.logger.log(f"Processing payment of ${amount:.2f}")
        print(f"Payment of ${amount:.2f} processed successfully.")

# Demonstration
if __name__ == "__main__":
    console_logger = ConsoleLogger()
    file_logger = FileLogger()

    # Using console logger
    payment1 = PaymentProcessor(console_logger)
    payment1.process_payment(100.50)

    # Using file logger
    payment2 = PaymentProcessor(file_logger)
    payment2.process_payment(250.75)
