class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name !r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Device Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} Pages Remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your Device is not Connected")
            return
        print(f"Printing {pages} Pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()

