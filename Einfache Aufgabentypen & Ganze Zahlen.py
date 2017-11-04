#Erzeugung Ganzzahlige Zahlen

from random import *

def integerZahl():
    
    liste = [randint(0,20)]
    ergebnis = 0
    for i in range(len(liste)):
            ergebnis+= liste[i] *10**-i
    return ergebnis

#Instanzierung der Einfachen Aufgabentypen

def PlusEinfach():
    x = integerZahl()
    y = integerZahl()
    z = str(x) + str(' ') + str('+') + str(' ') + str(y)
    return z

print(PlusEinfach())


def MinusEinfach():
    x = integerZahl()
    y = integerZahl()
    z = str(x) + str(' ') + str('-') + str(' ') + str(y)
    return z

print(MinusEinfach())

def MalEinfach():
    x = integerZahl()
    y = integerZahl()
    z = str(x) + str(' ') + str('*') + str(' ') + str(y)
    return z

print(MalEinfach())

def GeteiltEinfach():
    x = integerZahl()
    y = integerZahl()
    z = str(x) + str(' ') + str(':') + str(' ') + str(y)
    return z

print(GeteiltEinfach())
