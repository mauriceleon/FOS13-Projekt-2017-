from random import *



def real():
    
    liste = [randint(0,10), randint(0,9), randint(1,9)]
    ergebnis = 0
    for i in range(len(liste)):
            ergebnis+= liste[i] *10**-i
    return ergebnis


print(real())