#Exo 1

print("Exercice 1") 
print ("veuillez saisir deux nombres")
x=int(input())
y=int(input())
print(f"la premiere valeur saisi est : {x}")
print(f"la derniere valeur saisie est : {y}")
a=x
x=y
y=a
print(f"la premiere valeur devient  : {x}")
print(f"la derniere valeur devient  : {x}")

#Exo 2

print("Exercice 2") 
print ("veuillez saisir un nombre")
x=int(input())
print(f"Le carré de ",x," est {x*x}:")


#Exo 3


print("Exercice 2") 
print ("veuillez saisir le prix HT de l'article")
prixHT=int(input())
nbr=int(input(print("veuillez saisir le nombre d'article")))
TVA=float(input(print("veuillez saisir le taux de la tva (18% correspond à 0.18)")))
print(f"le prix tout taxe compris est : {prixHT*nbr*(1+TVA)} Fcfa")


#Exo 4

print("Exercice 4")
print("Saisir deux nombres")
x=int(input())
y=int(input())
if(x>0 and y<0) or(x<0 and y>0):
    print(f"le produit de {x} et {y} est négatif")
else:
    print(f"le produit de {x} et {y} est positif")

    
#exo 5

print ("Exercice 5")
print("Veuillez saisir l'age de l'enfant")
age = int(input())
if(age<=7):
    print("Poussin")
elif (age<=9):
    print("Pupille")
elif (age<=11):
    print("Minime")
elif (age>=12):
    print("Cadet")
 

#exo10
print(1+2+3+4+5)

print("Saisir le nombre de notes")
nbr = int(input())
print(f"Saisir les {nbr} notes")
i = compt = 0
note = [] 
while(i<nbr):
    print(f"saisir la note {i}")
    note.append(int(input()))
    i+=1
print(f"La moyenne générale de la classe est : {sum(note)/len(note)}")
for i in note:
    if i>sum(note)/len(note):
        compt+=1
print(f"Il existe {compt} note supérieur à la moyenne qui est {sum(note)/len(note)}")

