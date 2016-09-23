## hangman(word, guesses): this is a game hangman. Anyone can enter a word, word 
## which will be what the user has to figure out and a number, guesses, which
## represents the amount of times the user can make a wrong guess. If the user
## chooses a letter that is a part of the word, the amount of guesses will not 
## decrease. The user will enter a letter each round and the hidden word will
## be printed back to the user each time, showing the user if the letter was 
## a part of the word or not. If the user is not able to get the right word in
## the certain amount of guesses, the user loses and the game then closes. The
## user can quit at anytime simply by writing quit when prompted.

## Effects: Prints out a greeting, the amount of guesses the user currently has
## what the word looks like after his/her guesses, and also prints out if 
## the letter the user inputted has been inputted before or not. 

## hangman: Str Nat -> None

def hangman(word, guesses):
    unknownword = len(word) * "-"
    guessedletters = []
    print ("Welcome to hangman.")
   
    while guesses > 0:
        
        
        print ("Your word is " + unknownword)
        check = input("Please guess a letter or type quit: ")
            
            
        if check == "quit":
            print ("Goodbye!")
            break
            
        if guesses == 1 and word.find(check) == -1:
            print ("Game over. The correct word is " + word + ".")
            break    
            
        if check.isalpha() == True:
            if check in guessedletters:
                print ("You already guessed " + check + "." +
                            " Guesses remaining: " + str(guesses))
            else:
                
                guessedletters.append(check)
                if word.find(check) == -1:
                    guesses = guesses - 1
                    print("Sorry, try again. Guesses remaining: " + str(guesses))
                    
                    print ("\n")
                else:
                    for i in range (len(word)):
                        if word[i] == check:
                            unknownword = unknownword[0:i] + check + unknownword[(i+1):]
                    if unknownword == word:
                        print ("Congratulations the word is " + word + ".")
                        break
                                
                    print ("")
                        
            
        
                        
                    

    
                
            
        