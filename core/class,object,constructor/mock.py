# Create an abstract base Item and one concrete subclass Book:
# • Item requires get_summary().
# • Book stores title, private _metadata dict, protected _available flag. Use properties to safely
# read metadata.
# • Include a shared catalog_tag and a way to update it globally.
# • Add a pricing method with a default parameter discount=0.
# • Include str and repr.
# • Add a small validator for metadata keys.
# Create books, print str/repr, update shared tag, shallow copy & deepcopy the book list and
# show differences.
from abc import ABC,abstractmethod
class Item(ABC):
    @abstractmethod
    def get_summary(self):
        print("summ")
class Book(Item):
    def __init__(self,title,metadata_dict,available_flag):
        self.title=title
        self.__metadata_dict=23
        self._available_flag=available_flag
