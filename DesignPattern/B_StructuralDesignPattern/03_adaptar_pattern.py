# Target interface
class Printer:
    def print(self, text):
        pass

# Adaptee
class LegacyPrinter:
    def print_document(self, text):
        print("Legacy printer printing:", text)

# Adapter
class LegacyPrinterAdapter(Printer):
    def __init__(self, legacy_printer):
        self.legacy_printer = legacy_printer

    def print(self, text):
        self.legacy_printer.print_document(text)

# Client code
legacy_printer = LegacyPrinter()
adapter = LegacyPrinterAdapter(legacy_printer)
adapter.print("Hello, world!")


# ==================================================

class WeightMachine:
    def get_weight_in_kg(self):
        pass

# Adaptee
class WeightMachineAdaptee:
    def get_weight_in_pound(self):
        return 30

# Adapter
class WeightMachineAdapter(WeightMachine):
    def __init__(self, weightMachineAdaptee):
        self.weightMachineAdaptee = weightMachineAdaptee

    def get_weight_in_kg(self):
        weight_in_pound = self.weightMachineAdaptee.get_weight_in_pound()
        return weight_in_pound * 45


# Client code
weightMachineAdaptee = WeightMachineAdaptee()
adapter = WeightMachineAdapter(weightMachineAdaptee)
print(adapter.get_weight_in_kg())



# ============================================================

# Target interface
class Printer:
    def print(self, text):
        pass

# Adaptee
class OldPrinter:
    def print_document(self, text):
        print(f"Old Printer: {text}")

# Adapter
class PrinterAdapter(Printer):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        self.old_printer.print_document(text)

# Client code
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)

adapter.print("Hello, world!")
