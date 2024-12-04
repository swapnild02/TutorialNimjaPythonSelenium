from abc import ABC,abstractmethod

class  HomePageInterface(ABC):

    def __init__(self,driver):
        pass

    @abstractmethod
    def enter_product_into_search_box_field(self,product_name):
        pass

    @abstractmethod
    def text(self):
        pass