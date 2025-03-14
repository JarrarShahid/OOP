# interface_segregation.py

from abc import ABC, abstractmethod

# Separate interfaces
class Printer(ABC):
    @abstractmethod
    def print_document(self, document: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self) -> str:
        pass

class Fax(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass


# Class that implements only printing functionality
class BasicPrinter(Printer):
    def print_document(self, document: str):
        print(f"Printing document: {document}")

# Class that implements printing and scanning
class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document: str):
        print(f"Printing document: {document}")

    def scan_document(self) -> str:
        return "Scanned document content"

# Class that implements all three functionalities
class AllInOnePrinter(Printer, Scanner, Fax):
    def print_document(self, document: str):
        print(f"Printing document: {document}")

    def scan_document(self) -> str:
        return "Scanned document content"

    def send_fax(self, document: str):
        print(f"Sending fax: {document}")


# Demonstration
if __name__ == "__main__":
    basic_printer = BasicPrinter()
    basic_printer.print_document("Basic Printer Test")

    mf_printer = MultiFunctionPrinter()
    mf_printer.print_document("MFP Test")
    print(mf_printer.scan_document())

    aio_printer = AllInOnePrinter()
    aio_printer.print_document("AIO Test")
    print(aio_printer.scan_document())
    aio_printer.send_fax("Fax Test")
