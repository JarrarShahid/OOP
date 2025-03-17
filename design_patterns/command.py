# command.py

from abc import ABC, abstractmethod

# Step 1: Command Interface
class Command(ABC):
    """Abstract Command class."""
    
    @abstractmethod
    def execute(self):
        """Executes the command."""
        pass

    @abstractmethod
    def undo(self):
        """Undoes the command."""
        pass


# Step 2: Concrete Commands
class WriteCommand(Command):
    """Command to write text."""
    
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.write(self.text)

    def undo(self):
        self.editor.remove_last()


class UndoCommand(Command):
    """Command to undo last action."""
    
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.undo()


class RedoCommand(Command):
    """Command to redo last undone action."""
    
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.redo()


# Step 3: Receiver - Text Editor
class TextEditor:
    """A simple text editor with undo/redo functionality."""
    
    def __init__(self):
        self.text = []
        self.history = []
        self.redo_stack = []

    def write(self, text):
        """Writes text and saves history."""
        self.text.append(text)
        self.history.append(text)
        self.redo_stack.clear()  # Clear redo stack on new action

    def remove_last(self):
        """Removes the last written text."""
        if self.text:
            removed = self.text.pop()
            self.redo_stack.append(removed)

    def undo(self):
        """Undoes the last action."""
        if self.text:
            removed = self.text.pop()
            self.redo_stack.append(removed)

    def redo(self):
        """Redoes the last undone action."""
        if self.redo_stack:
            self.text.append(self.redo_stack.pop())

    def get_text(self):
        """Returns current text as a string."""
        return "".join(self.text)


# Step 4: Invoker - Command Executor
class CommandExecutor:
    """Invoker that executes commands."""
    
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        """Executes and stores command history."""
        command.execute()
        self.history.append(command)

    def undo_last(self):
        """Undoes the last command."""
        if self.history:
            last_command = self.history.pop()
            last_command.undo()


# Step 5: Demonstration
if __name__ == "__main__":
    editor = TextEditor()
    executor = CommandExecutor()

    print("Typing 'Hello '")
    cmd1 = WriteCommand(editor, "Hello ")
    executor.execute_command(cmd1)
    print("Current Text:", editor.get_text())

    print("Typing 'World!'")
    cmd2 = WriteCommand(editor, "World!")
    executor.execute_command(cmd2)
    print("Current Text:", editor.get_text())

    print("Undo Last Action")
    undo_cmd = UndoCommand(editor)
    executor.execute_command(undo_cmd)
    print("Current Text:", editor.get_text())

    print("Redo Last Action")
    redo_cmd = RedoCommand(editor)
    executor.execute_command(redo_cmd)
    print("Current Text:", editor.get_text())

