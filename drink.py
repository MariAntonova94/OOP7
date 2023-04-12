from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name, volume, sugar, milk):
        self.name = name
        self.volume = volume
        self.sugar = sugar
        self.milk = milk

    def __str__(self) -> str:
        return f"{self.name}; Обьем кофе: {self.volume}; Сахар1: {self.sugar}; Молоко1: {self.milk};"


    def Drink(self, name, volume, sugar, milk):
        pass


