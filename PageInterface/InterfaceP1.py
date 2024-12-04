from abc import ABC,abstractmethod

class InterfaceP1:

    @abstractmethod
    def hello(self):
        pass


class C1(InterfaceP1):

    def hello(self):
        print("Hello")

IP=C1()
IP.hello()
