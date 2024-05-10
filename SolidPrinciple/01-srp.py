# Single Responsibility Principle


# Without srp
class FileManager:
    def read(self, encoding="utf-8"):
        pass
    def write(self, data, encoding="utf-8"):
        pass
    def compress(self):
        pass
    def decompress(self):
        pass



# With SRP
class FileManager:
    def read(self, encoding="utf-8"):
        pass
    def write(self, data, encoding="utf-8"):
        pass
class ZipFileManager:
    def compress(self):
        pass
    def decompress(self):
        pass

