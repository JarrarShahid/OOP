

class Report:
    """A class that stores report data."""
    
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_report_data(self):
        """Return the report's data."""
        return f"Title: {self.title}\nContent: {self.content}"


class ReportPrinter:
    """A class responsible for printing reports."""

    @staticmethod
    def print_report(report):
        """Prints the report details."""
        print("----- Report -----")
        print(report.get_report_data())
        print("------------------")


# Demonstration
if __name__ == "__main__":
    # Creating a report object
    report = Report("Monthly Sales", "Sales increased by 20% this month.")

    # Printing the report using ReportPrinter
    printer = ReportPrinter()
    printer.print_report(report)
