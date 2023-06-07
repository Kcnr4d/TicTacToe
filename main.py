import random
def introduce():
    print("Witaj w grze kółko i krzyżyk! Aby zagrać wprowadź nazwy obu graczy, jeżeli chcesz grać z komputerem, graczowi drugiemu nadaj nazwę 'computer'")
    name1 = input("Wprowadź nazwę 1 gracza(X):\n")
    name2 = input("Wprowadź nazwę 2 gracza(O):\n")
    printmap(name1, name2)


def printmap(name1, name2):
    tab = {}

    for i in range(9):
        tab[i] = "|.|"

    print("\t 1\t 2\t 3\nA\t|.|\t|.|\t|.|\nB\t|.|\t|.|\t|.|\nC\t|.|\t|.|\t|.|\n")
    counter = 0
    ask(name1, name2, counter, tab)


def updatemap(case, tab, counter, name1, name2):
    position = 0
    if name2 == "computer" and counter % 2 == 1:
        posistion = case
    else:
        xaxis = case[1:2]
        yaxis = case[:1]
        if yaxis == 'A':
            yaxis = 0
        elif yaxis == 'B':
            yaxis = 3
        elif yaxis == 'C':
            yaxis = 6
        else:
            print("Podaj poprawne dane!")
            ask(name1, name2, counter, tab)

        if len(case) != 2:
            print("Podaj poprawne dane!")
            ask(name1, name2, counter, tab)

        if int(xaxis) < 0 or int(xaxis) > 3:
            print("Podaj poprawne dane!")
            ask(name1, name2, counter, tab)

        posistion = int(yaxis) + int(xaxis) - 1

    if tab[posistion] == "|.|":
        if counter % 2 == 0:
            tab[posistion] = '|X|'
        else:
            tab[posistion] = '|O|'
    else:
        print("To pole jest już zajęte!")
        ask(name1, name2, counter, tab)

    print("\t 1\t 2\t 3\nA", tab[0], tab[1], tab[2], sep="\t")
    print("B", tab[3], tab[4], tab[5], sep="\t")
    print("C", tab[6], tab[7], tab[8], sep="\t")
    counter += 1
    if checkvictory(tab):
        if counter % 2 == 0:
            print("Wygrał gracz " + name2)
            introduce()
        else:
            print("Wygrał gracz " + name1)
            introduce()
    else:
        draw = True
        for i in range(9):
            if tab[i] == "|.|":
                draw = False

        if draw:
            print("Remis")
            introduce()
        else:
            ask(name1, name2, counter, tab)


def ask(name1, name2, counter, tab):
    if name2 != "computer":
        if counter % 2 == 0:
            player = name1
        else:
            player = name2
        case = input("Player " + player + " , mark position: ")
    else:
        if counter % 2 == 0:
            player = name1
            case = input("Player " + player + " , mark position: ")
        else:
            case1 = 'A1'
            if(trywin(tab) != -1):
                case = trywin(tab)
            else:
                case = random.randrange(0, 8)
            if case == 0:
                case1 = 'A1'
            elif case == 1:
                case1 = 'A2'
            elif case == 2:
                case1 = 'A3'
            elif case == 3:
                case1 = 'B1'
            elif case == 4:
                case1 = 'B2'
            elif case == 5:
                case1 = 'B3'
            elif case == 6:
                case1 = 'C1'
            elif case == 7:
                case1 = 'C2'
            elif case == 8:
                case1 = 'C3'
            print("Komputer wybrał: " + case1)

    updatemap(case, tab, counter, name1, name2)


def checkvictory(tab):
    if tab[0] == tab[1] == tab[2] != "|.|":
        return True
    elif tab[3] == tab[4] == tab[5] != "|.|":
        return True
    elif tab[6] == tab[7] == tab[8] != "|.|":
        return True
    elif tab[0] == tab[3] == tab[6] != "|.|":
        return True
    elif tab[1] == tab[4] == tab[7] != "|.|":
        return True
    elif tab[2] == tab[5] == tab[8] != "|.|":
        return True
    elif tab[0] == tab[4] == tab[8] != "|.|":
        return True
    elif tab[2] == tab[4] == tab[6] != "|.|":
        return True


def trywin(tab):
    if tab[0] == tab[1] != "|.|" and tab[2] == "|.|":
        return 2
    elif tab[0] == tab[2] != "|.|" and tab[1] == "|.|":
        return 1
    elif tab[2] == tab[1] != "|.|" and tab[0] == "|.|":
        return 0
    elif tab[3] == tab[4] != "|.|" and tab[5] == "|.|":
        return 5
    elif tab[3] == tab[5] != "|.|" and tab[4] == "|.|":
        return 4
    elif tab[5] == tab[4] != "|.|" and tab[3] == "|.|":
        return 3
    elif tab[6] == tab[7] != "|.|" and tab[8] == "|.|":
        return 8
    elif tab[6] == tab[8] != "|.|" and tab[7] == "|.|":
        return 7
    elif tab[8] == tab[7] != "|.|" and tab[6] == "|.|":
        return 6
    elif tab[0] == tab[3] != "|.|" and tab[6] == "|.|":
        return 6
    elif tab[0] == tab[6] != "|.|" and tab[3] == "|.|":
        return 3
    elif tab[6] == tab[3] != "|.|" and tab[0] == "|.|":
        return 0
    elif tab[1] == tab[4] != "|.|" and tab[7] == "|.|":
        return 7
    elif tab[1] == tab[7] != "|.|" and tab[4] == "|.|":
        return 4
    elif tab[7] == tab[4] != "|.|" and tab[1] == "|.|":
        return 1
    elif tab[2] == tab[5] != "|.|" and tab[8] == "|.|":
        return 8
    elif tab[2] == tab[8] != "|.|" and tab[5] == "|.|":
        return 5
    elif tab[8] == tab[5] != "|.|" and tab[2] == "|.|":
        return 2
    elif tab[0] == tab[4] != "|.|" and tab[8] == "|.|":
        return 8
    elif tab[0] == tab[8] != "|.|" and tab[4] == "|.|":
        return 4
    elif tab[8] == tab[4] != "|.|" and tab[0] == "|.|":
        return 0
    elif tab[2] == tab[4] != "|.|" and tab[6] == "|.|":
        return 6
    elif tab[2] == tab[6] != "|.|" and tab[4] == "|.|":
        return 4
    elif tab[6] == tab[4] != "|.|" and tab[2] == "|.|":
        return 2
    else:
        return -1


introduce()
