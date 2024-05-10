# High level modules should not depend upon low level details.Depend upon abstractions, not concretions.
# high-level modules (which contain the main business logic) should not depend on low-level modules (details of implementation);
#  instead, both should depend on abstractions

# Violating DIP
class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
    
class FrontEnd:
    def __init__(self, back_end: BackEnd):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)



# If we want to add add another type of data source, we have to modify the BackEnd class 
#  Both classes are tightly coupled. This coupling can lead to scalability issues. 
# For example, if we want the app to read data from a REST API. 
# we can add a new method to BackEnd to retrieve the data from the REST API. 
# However, that will also require us to modify FrontEnd, which has already tested and closed to modification



# Applying DIP

from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class FrontEnd:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source   # Dependency injection

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"
    
if __name__ == "__main__":

    db_front_end = FrontEnd(Database())
    db_front_end.display_data()

    api_front_end = FrontEnd(API())
    api_front_end.display_data()



# Violating DIP
class Database():
    def get_data(self):
        return "Data from the database"
    
class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source 

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)