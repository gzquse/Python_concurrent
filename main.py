# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC,abstractmethod


class machine(ABC):

    @abstractmethod
    def hello(self):
        print('machine')


class computer(machine, ABC):

    def hello(self):
        super(computer, self).hello()
        print('computer')


com = computer()
com.hello()