import seminar7
import copy
import drink
from seminar7.drink import Drink


class Coffe:

    all = []
    drink = Drink("Латте", 250, 15, 200)
    all.append(copy.copy(drink))
    drink = Drink("Капучино", 300, 20, 250)
    all.append(copy.copy(drink))
    drink = Drink("Американо", 200, 10, 160)
    all.append(copy.copy(drink))
    drink = Drink("Эспрессо", 70, 0, 0)
    all.append(copy.copy(drink))
