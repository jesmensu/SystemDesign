# Subsystem classes
class CPU:
    def freeze(self):
        print("CPU: Freezing")

    def jump(self, position):
        print(f"CPU: Jumping to {position}")

    def execute(self):
        print("CPU: Executing")

class Memory:
    def load(self, position, data):
        print(f"Memory: Loading data '{data}' to position {position}")

class HardDrive:
    def read(self, lba, size):
        print(f"Hard Drive: Reading {size} bytes from LBA {lba}")

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0, "boot_loader")
        self.cpu.jump(0)
        self.cpu.execute()
        self.hard_drive.read(0, 1024)

# Client code
computer = ComputerFacade()
computer.start()
