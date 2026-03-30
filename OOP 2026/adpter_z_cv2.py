
class OldPrinter:
    def print_text(self, text):
        print(text)


class Printer:
    def print(self, message):
        ...
 
class Adapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, message):
        self.old_printer.print_text(message)


if __name__ == "__main__":
    old_printer = OldPrinter()
    adapter = Adapter(old_printer)
    adapter.print("Hello, World!")