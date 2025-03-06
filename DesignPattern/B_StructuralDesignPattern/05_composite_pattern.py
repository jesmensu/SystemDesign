from abc import ABC, abstractmethod

# Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def ls(self):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def ls(self):
        print(f"File: {self.name}")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def ls(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.ls()

# Client code
# Creating files
file1 = File("file1.txt")
file2 = File("file2.txt")
file3 = File("file3.txt")

# Creating directories
dir1 = Directory("dir1")
dir2 = Directory("dir2")

# Adding files to directories
dir1.add(file1)
dir1.add(file2)
dir2.add(file3)

# Adding directories to directories
root = Directory("root")
root.add(dir1)
root.add(dir2)

# Listing contents of root directory
root.ls()
