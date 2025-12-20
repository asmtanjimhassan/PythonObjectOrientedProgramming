""" If the subclass is derived from Abstract Class,
each abstract methods must be overwritten

We cannot create object for Abstract class"""

from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def method1(self):
        pass

class B(A):
    def __init__(self):
        pass

    def method1(self):
        print("Overwriting the abstract method")

a = B()
a.method1()
