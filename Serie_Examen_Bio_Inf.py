"""import os
print("Exercice 1")
print("Veuillez saisir un entier p")
p = int(input())
print("Veuillez saisir un entier q")
q = int(input())
fichier = open("fic-sortie.txt", "w")
fichier.write(f"\nLes couples (x,y) avec 1<x<p et 1<x<q")
fichier.write(f"\np = {p} et q = {q}")
for i in range (1,p+1):
    fichier.write("\n")
    for j in range (1,q+1):
        fichier.write(f"({i} , {j})")
fichier.write("\n")
fichier.close()
# récupérer le chemin du répertoire courant
path = os.getcwd()
print(f"Pour voir le résultat, merci d'ouvrir le fichier fic-sortie.txt dans le répertoire : {path}")        
"""

from dataclasses import dataclass
from re import I
from unicodedata import name
from xmlrpc.client import boolean

@dataclass
class Personne:
    name: str
    surname: str
    age: int
    poids: int
    code : int

personne = []

def creation_personne():
    print("combien de personne voulez vous ajouter?")
    nbrP = int(input())
    
    for i in range(0,nbrP):
        p = Personne(name='',surname='',age=0,poids=0,code=0)
        p.name = input("Saisir le nom")
        p.surname = input("Saisir le surnom")
        p.age = int(input("saisir son age"))
        p.poids = int(input("saisir son poids"))
        p.code = int(input("Saisir son code"))
        personne.append(p)


def afficher(a : int):
    if(0 < a < len(personne)):
        print(f"La personne se trouve à la position {a}")
        print(f"Nom :{personne[a].name}")
        print(f"Surname :{personne[a].surname}")
        print(f"Âge :{personne[a].age}")
        print(f"Poids :{personne[a].poids}")
        print(f"Code :{personne[a].code}")
    else :
        print(f"Veuillez saisir un nombre compris entre 0 et {len(personne)}")
        x = int(input())
        afficher(x)

 
def afficher_tout():
    cmpt = 0
    for i in personne:
        print(f"Personne n°{cmpt}")
        print(f"Nom :{i.name}")   
        print(f"Surname :{i.surname}")    
        print(f"Âge :{i.age}")    
        print(f"Poids :{i.poids}")    
        print(f"Code :{i.code}")    

        
def update(a : int):
    afficher(a)
    if(0 < a < len(personne)):
        print(f"La personne se trouve à la position {a}")
        print(f"Nom :{personne[a].name}")
        print(f"Surname :{personne[a].surname}")
        print(f"Âge :{personne[a].age} ans")
        print(f"Poids :{personne[a].poids} kg")
        print(f"Code :{personne[a].code}")
        
    print("Veuillez saisir l'âge")
    personne[a].age = int(input())
    personne[a].poids = int(input())
        
    print("Apres modification on a :")
    afficher(a)
   
def supprimer_personne():
    afficher_tout()
    print("Saisir la position de la personne à supprimer")
    a = int(input())
    print(f"vous voulez supprimer la personne à la position {a} o/n")
    reponse = input()
    if (reponse == "o"):
        del personne[a]
    else :
        print("SUppression annulée")



x = ["a","d","e"]

for i in x:
    print(i)

x.clear(x[1])
for i in x:
    print(i)