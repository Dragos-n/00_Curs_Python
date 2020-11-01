import random
WordList = ["singur", "vocale", "obligatie", "propulsat", "romanesc", "treieratoarei", "streang", "trunchi", "ghiont",
            "stramt", "strans", "strict", "zbenghi", "sfincsi", "prompt", "transplant", "avion", "apartament"]
GameRetry = 7
HangmanWord = random.choice(WordList)
ShownWord = HangmanWord[0]
LastFoundPosition = 1


def word_init(shownword: str, hangmanword: str) -> str:
    """

    :param shownword: Cuvantul ajutator printat pe ecran
    :param hangmanword: Cuvantul care trebuie ghicit
    :return: Print de cuvantul ajutator initial
    """
    for AuxCounter in range(1, len(hangmanword)):
        if hangmanword.find(hangmanword[0], AuxCounter, AuxCounter + 1) != -1:
            shownword = shownword + hangmanword[0]
        else:
            shownword = shownword + " _ "
    print("        {}".format(shownword))
    return shownword


def game_main(gameretry: int, shownword: str, hangmanword: str) -> str:
    """

    :param gameretry: numarul de litere gresit permise
    :param shownword: Cuvantul ajutator printat pe ecran - folosit si pentru verificarea vitoriei
    :param hangmanword: Cuvantul care trebuie ghicit
    :return: Rezultatul final al jocului: Victorie repsectiv joc pierdut
    """
    while True:
        charaux = input("Indtroduceti o noua litera: ")
        if shownword.find(charaux, 1) != -1:
            print("Acesasta litera a fost deja introdusa!")
        elif hangmanword.find(charaux, 0) == -1:
            print("WRONG!!!")
            gameretry -= 1
        elif shownword.find(charaux, 1) == -1 and hangmanword.find(charaux, 1) != -1:
            tempshowword = char_replace(shownword, hangmanword, charaux).replace(" ", "")
            shownword = tempshowword
        if shownword == hangmanword:
            return "VICTORIE!  Cuvantul a fost: *** {} ***".format(HangmanWord)
        if gameretry == 0:
            return "Ai pierdut! Mai baga o fisa!"


def char_replace(shownword: str, hangmanword: str, charaux: str) -> str:
    """

    :param shownword: Cuvantul ajutator printat pe ecran
    :param hangmanword: Cuvantul care trebuie ghicit
    :param charaux: Caracterul care se afla in cunvatul care trebuie ghicit
    :return: Noul cuvant ajutatore, in care a fost inlocuit spatiul liber cu actualul caracter corect introdus
    """
    lastfoundposition = 0
    while hangmanword.find(charaux, lastfoundposition,) != -1:
        lastfoundposition = hangmanword.find(charaux, lastfoundposition)
        auxlist = list(shownword.replace(" ", ""))
        auxlist[lastfoundposition] = charaux
        lastfoundposition += 1
        shownword = " ".join(auxlist)
    print("Corect! \n        {}".format(shownword))
    return shownword


def main():
    helpword = word_init(ShownWord, HangmanWord)
    print(game_main(GameRetry, helpword, HangmanWord))


main()
