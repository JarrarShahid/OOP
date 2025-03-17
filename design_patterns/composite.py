# composite.py

from abc import ABC, abstractmethod


# Step 1: Component Interface
class FileSystemComponent(ABC):
    """Abstract base class for both File and Folder."""

    @abstractmethod
    def show_details(self, indent=0):
        """Displays the details of the component."""
        pass


# Step 2: Leaf (File)
class File(FileSystemComponent):
    """Represents a file in the system."""

    def __init__(self, name, size):
        self.name = name
        self.size = size  # in KB

    def show_details(self, indent=0):
        """Displays file details."""
        print("  " * indent + f"📄 File: {self.name} ({self.size} KB)")


# Step 3: Composite (Folder)
class Folder(FileSystemComponent):
    """Represents a folder that can contain files and other folders."""

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        """Adds a file or subfolder to this folder."""
        self.children.append(component)

    def show_details(self, indent=0):
        """Displays folder details and its contents recursively."""
        print("  " * indent + f"📁 Folder: {self.name}")
        for child in self.children:
            child.show_details(indent + 1)


# Step 4: Demonstration
if __name__ == "__main__":
    # Creating files
    file1 = File("resume.pdf", 120)
    file2 = File("report.docx", 300)
    file3 = File("photo.jpg", 2048)

    # Creating folders
    documents = Folder("Documents")
    pictures = Folder("Pictures")
    main_folder = Folder("Main Folder")

    # Organizing files and folders
    documents.add(file1)
    documents.add(file2)
    pictures.add(file3)
    
    main_folder.add(documents)
    main_folder.add(pictures)

    # Displaying the file system hierarchy
    print("\n📂 File System Structure:\n")
    main_folder.show_details()
