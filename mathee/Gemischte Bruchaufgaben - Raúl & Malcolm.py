from random import *
r = randint(1, 3)
Nenner1=randint(1, 20)
Zähler1=randint(1, 20)
Nenner2=randint(1, 20)
Zähler2=randint(1, 20)
NeuerNenner1=Nenner1*Nenner2
NeuerZähler1=Zähler1*Nenner2
NeuerNenner2=Nenner2*Nenner1
NeuerZähler2=Zähler2*Nenner1
if r == 1:
  z3=NeuerZähler1+NeuerZähler2
  n3=NeuerNenner1
  print("add")
  op=("+")
elif r == 2:
  z3=NeuerZähler1-NeuerZähler2
  n3=NeuerNenner1
  print("sub")
  op=("-")
elif r == 3:
  z3=Zähler1*Zähler2
  n3=Nenner1*Nenner2
  print("mult")
  op=("*")
if z3 == 0:
  print(Zähler1,op,Zähler2)
  print(Nenner1,op,Nenner2)
  print("-----")
  print("0,NULL")  
else:
  for x in range(400,1,-1):
    if (z3 % x == 0) and (n3 % x == 0):
      print(Zähler1,op,Zähler2)
      print(Nenner1,op,Nenner2)
      print("-----")
      print(int(z3/x))
      print(int(n3/x))
      break