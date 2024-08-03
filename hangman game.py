import random
countries=["pakistan","iran","oman","uzbekistan","india","japan","china","bhutan","nepal","egypt","france"]
randomword=random.choice(countries)
randomword_to_check=randomword
guessed_correctly=False
print("Welcome to the hangman game with a new hard version:")
for i in range(len(randomword)):
    print("_",end=" ")
print() 
for j in range(len(randomword)):
    letter=input("enter the letter to complete the word(It is the name of a country):").lower()
    if letter in randomword:
        particular_letter=randomword.index(letter)
        randomword=randomword.replace(randomword[particular_letter],"+")
        print("The letter is at the position:",particular_letter+1)
    print("you have left ",(len(randomword)-1)-j,"chances behind")
for k in range(len(randomword_to_check)):
    if randomword_to_check[k]==randomword[k]:
        print("You guessed wrong")
        print("The correct word was:",randomword_to_check)
        guessed_correctly=False
        break
    elif randomword_to_check[k] !=randomword[k]:
        guessed_correctly=True
if guessed_correctly:
    print("you guessed correct")
    print("The word was :",randomword_to_check)

