import copy
import coffe
from seminar7.drink import Drink

def addLattee():

    name = "Латте"
    volume = int(input("Обьем Латте: "))
    sugar = int(input("Сахар : "))
    milk = input("Молоко : ")

    drink = Drink(name, volume, sugar, milk)
    coffe.Coffe.all.append(copy.copy(drink))

def addKapuchino():
    name = "Капучино"
    volume = int(input("Обьем Капучино: "))
    sugar = int(input("Сахар : "))
    milk = input("Молоко : ")

    drink = Drink(name, volume, sugar, milk)
    coffe.Coffe.all.append(copy.copy(drink))

def addAmericano():
    name = "Американо"
    volume = int(input("Обьем Американо: "))
    sugar = int(input("Сахар : "))
    milk = input("Молоко : ")

    drink = Drink(name, volume, sugar, milk)
    coffe.Coffe.all.append(copy.copy(drink))

def addEspresso():
    name = "Эспрессо"
    volume = int(input("Обьем Эспрессо: "))
    sugar = int(input("Сахар : "))
    milk = input("Молоко : ")

    drink = Drink(name, volume, sugar, milk)
    coffe.Coffe.all.append(copy.copy(drink))

def showAll():
    for i in range(len(coffe.Coffe.all)):
        print(f"{i+1}) {coffe.Coffe.all[i]}")


