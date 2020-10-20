import random
WordList = ["singur", "vocale", "obligatie", "propulsat", "romanesc", "treieratoarei", "streang", "trunchi", "ghiont",
            "stramt", "strans", "strict", "zbenghi", "sfincsi", "prompt", "transplant", "avion", "apartament"]
GameRetry = 7
HangmanWord = random.choice(WordList)
ShownWord = HangmanWord[0]
LastFoundPosition = 1
for AuxCounter in range(1, len(HangmanWord)):
    if HangmanWord.find(HangmanWord[0], AuxCounter, AuxCounter + 1) != -1:
        ShownWord = ShownWord + HangmanWord[0]
    else:
        ShownWord = ShownWord + " _ "
print("        {}".format(ShownWord))

while True:
    LastFoundPosition = 0
    CharAux = input("Indtroduceti o noua litera: ")
    if ShownWord.find(CharAux,1) != -1:
        print("Acesasta litera a fost deja introdusa!")
    elif HangmanWord.find(CharAux, 0) == -1:
        print("WRONG!!!")
        GameRetry -= 1
        if GameRetry == 0:
            print("Ai pierdut! Mai baga o fisa!")
            break
    else:
        while HangmanWord.find(CharAux, LastFoundPosition,) != -1:
            LastFoundPosition = HangmanWord.find(CharAux, LastFoundPosition)
            AuxList = list(ShownWord.replace(" ", ""))
            AuxList[LastFoundPosition] = CharAux
            LastFoundPosition += 1
            ShownWord = " ".join(AuxList)
        if ShownWord.replace(" ", "") == HangmanWord:
            print("VICTORIE!  Cuvantul a fost: *** {} ***".format(HangmanWord))
            break
        print("Corect! \n        {}".format(ShownWord))








