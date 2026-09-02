"""
#P1

#Q1

question1 = input("What's your first name : ")
question2 = input("What's your last name : ")

print("Hello Mr." + question1 + " " + question2)

#Q2

question1 = input("What's your name : ")
question2 = int(input("What's your wages per hour : "))
question3 = int(input("how much houres do you spend on work : "))

if(question3 >= 40) :
    salaire = question2 * (question3 * 1.5)
else :
    salaire = question2 * question3

print(salaire)

#Q3

question1 = int(input("how old are you : "))

if(question1 < 18) :
    print("l'entrée est refusée")
elif(question1 >= 18 and question1 < 25) :
    print("l'entrée est gratuite")
else :
    print("l'entrée est autorisée uniquement si elle est membre du club  ou accompagnée d'un membre.")
"""
#P2

#Q1

"""
question1 = int(input("Please enter a number : "))

for i in range(1, question1) :
    result = question1 * i
    print(result)



#Q2

question1 = input("please enter a string : ")
reversed_text = ""

for l in question1: 
    reversed_text = l + reversed_text
print(reversed_text)
#print(question1[::-1])
"""

"""La suite de Syracuse (aussi appelée suite de Collatz ou conjecture de Syracuse) est une suite définie pour un entier naturel positif n comme suit :

Si n est pair, le terme suivant est n // 2.

Si n est impair, le terme suivant est 3n + 1.

La suite se termine lorsque n devient égal à 1.

Écrire un code permettant de calculer cette suite"""

n = int(input("Please enter a number : "))
if(n == 1):
    print(n)
elif(n % 2 == 0) :
    n = n / 2
    print(n)
elif(n % 2 != 0) :
    n = 3 * n + 1
    print(n)
