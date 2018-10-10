#START
#import os
import random

print('\t=========================WELCOME TO THE HANGMAN GAME, INSHORT GUESS THE WORD GAME:==================================\n')


RealWords = ['SUN','FLOWER','BUTTERFLY','RIP','JEEP','FRUITE','MANGO','APPLE','MOON','ABILITY','ABLE','ABROAD','ABSENT','ABUSE','TWITTER','FACEBOOK','ACCIDENTALLY','ACCOUNT','ACROSS','ADD','ADULT','AFTER','AGE','AIM','AIR']
Words = random.choice(RealWords)

#RealWord = input('Write the Hangman Word in Capital Letters: ')

DisplayWord = ['_'] * len(Words) #PRINT THE BLANK SPACES IN LIST DEPEND UPON THE LENGTH OF WORDS
Input = '' #END WILL COME HERE, TO END THE GAME
GuessChances = 20 #CHANCES FOR USER TO GUESS THE LETTER
LetterNumber = 0  #COUNTER VARIABLE FOR LETTER NUMBER
CorrectGuess = 0  #COUNTER VARIABLE FOR CORRECT GUESS

#os.system('clear')

while(Input != 'END' and GuessChances != 0): #END WILL COME HERE, TO END THE GAME OR FINAL GUESS CHANCE 
    print('\t\t=======You have to fill this blank spaces with the Correct Letter to make correct word!!===========\n\n' '\t\t\t\t\t\t'+ str(DisplayWord))
    print('\n')
    print('\t\t===================================================================================================')
    print('\t\t\t\t=====================You have ' + str(GuessChances) + ' Guesses Left=============================')
    print('\t\t==================================================================================================\n\n')
    Input = input('Enter Letter in Capital Letters: ')


    while(LetterNumber < len(Words)):
        if(Words[LetterNumber] == Input): #COMPARE LETTER_NUMBER OF WORD WITH INPUT, AND SHOW LETTER THAN '_'
            DisplayWord[LetterNumber] = Input 
            CorrectGuess = CorrectGuess + 1 #GET INCREASE FOR NEXT LETTER
        LetterNumber = LetterNumber + 1 #WILL CHANGE THE LETTER NUMBER BY 1 EACH TIME

    GuessChances = GuessChances - 1 #CHANCES GETS DECREASES WITH EACH ATTEMPTS
    LetterNumber = 0 #ARRAY / LIST STARTS FROM ZERO 

    if (CorrectGuess == len(Words)): #COMPARE WITH LENGTH OF WORDS
          print('WINNER WINNER CHICKEN DINNER!! You Done It, You have won!!')
          break

    if (GuessChances == 0): #END OF ALL CHANCES
        print('Your are out of guesses. Game over! ')


#END
    
