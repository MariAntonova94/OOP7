import hotdrink
import menu
from seminar7 import coffe


def start():
    num = menu.menu()
    match num:
        case 1:
            addHotDrink()
        case 2:
            infoCoffe()
        case 3:
            exit()

def infoCoffe():
    hotdrink.showAll()

    start()

def addHotDrink():
    num = menu.hotdrink1()
    match num:
        case 1:
            hotdrink.addLattee()
        case 2:
            hotdrink.addKapuchino()
        case 3:
            hotdrink.addAmericano()
        case 4:
            hotdrink.addEspresso()
