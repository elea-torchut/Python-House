# Variables
E = int(input("Saisir le nombre de lignes : "))
L = 2*E
C = 2*E

# Scripte toit
for i in range(1,E+1) :
    for j in range(1,E-i+1):
        print("  ",end="")
    for j in range(1,2*i+1):
        if j == 1 :
            print("/ ",end="")
        elif j == 2*i :
            print("\ ",end="")
        else :
            print("  ",end="")
    print()

# Scripte carré
for i in range(1,L+1) :
    for j in range(1,C+1) :
        if i == 1 or i == L or j == 1 or j == C :
            print("°",end=" ")
        else :
            print(" ",end=" ")
    print()
print("Voici Ma Maison !!")
