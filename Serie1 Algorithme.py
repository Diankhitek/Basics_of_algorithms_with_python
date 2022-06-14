#Exo 5.1

print("Exercice 5.1") 
print ("veuillez saisir un nombre compris entre 1 et 3")
x=int(input())
while(x<1 or x>3):
    print("veuillez saisir un nombre compris entre 1 et 3 ")
    x= int(input())
print("le nombre saisit est :",x)

#Exo 2

print("Exercice 5.2") 
print ("veuillez saisir un nombre compris entre 10 et 20")
x=int(input())
while(x<10 or x>20):
    if (x<10):
        print("Plus grand")
    else :
        print("Plus petit")
    print("veuillez saisir un nombre compris entre 10 et 20 ")
    x= int(input())
print("le nombre saisit est :",x)


#Exo 3

print("Exercice 5.3") 
print ("veuillez saisir un nombre")
x=int(input())
y=x+10
while(x<=y):
    x+=1
    print(x)



#Exo 4

print("Exercice 5.4")
print ("veuillez saisir un nombre")
x=int(input())
for i in range(x+1,x+11):
    print(i)
    


#Exo 5

print("Exercice 5.5")
print("Ecrire un nombre")
x=int(input())
print("Table de multiplication par ",x)
for i in range (0,11):
    print(x," x ",i," = ",x*i)
    


#Exo 6

print("Exercice 5.6")
print("Ecrire un nombre")
x = int(input())
som=0
for i in range (1,x+1):
    som+=i
print("la somme des entiers est : ",som)

#exo 7

print("Exercice 5.7")
print("Ecrire un nombre")
x = int(input())
fact=1
for i in range (1,x+1):
    fact*=i
print(x,"! = ",fact)



#exo 8
'''
print("Exercice 5.8")
print("Nous allons saisir 20 nombres")
pg=0
for i in range (0,21):
    print("Saisir le nombre numéro ",i)
    x= int(input())
    if(x>pg):
        pg=x
        compt=i
print("le plus grand de ces nombres est :",pg)
print("La position du nombre est ",compt)

'''

#exo 9
'''
print("Exercice 5.9")

i=0
x=1
pg=0
while(x!=0):
    print("Saisir le nombre numéro ",i)
    x= int(input())
    if(x>pg):
        pg=x
        compt=i
    i+=1
print("le plus grand de ces nombres est :",pg)
print("La position du nombre est ",compt)

'''
#exo 11
'''
print("Exercice 5.9")

print("Ecrire un le nombre de chevaux entrants")
n = int(input())
print("Ecrire le nombre de chevaux sortants")
p = int(input())
nfact= pfact = npfact =1

for i in range (1,n+1):
    nfact*=i
for i in range (1,p+1):
    pfact*=i
for i in range (1,n-p+1):
    npfact*=i
    
print ("Dans l'ordre : une chance sur ",(nfact/npfact),' de gagner')
print ("Dans le désordre : une chance sur ",(nfact/(pfact*npfact)),' de gagner')

'''
#exo 11 simplifié

print("Exercice 5.11")

print("Ecrire un le nombre de chevaux entrants")
n = int(input())
print("Ecrire le nombre de chevaux sortants")
p = int(input())
pfact = n_npfact =1

for i in range (1,p+1):
    n_npfact *= n-p+i
    pfact *= i
print ("Dans l'ordre : une chance sur ",n_npfact,' de gagner')
print ("Dans le désordre : une chance sur ",n_npfact/pfact,' de gagner')
