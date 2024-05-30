# Target interface
class PrinterInterface:
    def print(self, text):
        pass

# Adaptee
class LegacyPrinter:
    def printDocument(self, text):
        print("Legacy printer printing:", text)

# Adapter
class Adapter(PrinterInterface):
    def __init__(self, legacy_printer):
        self.legacy_printer = legacy_printer

    def print(self, text):
        self.legacy_printer.printDocument(text)

# Client code
legacy_printer = LegacyPrinter()
adapter = Adapter(legacy_printer)
adapter.print("Hello, world!")
