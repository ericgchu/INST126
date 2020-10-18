import random

# Prints letters guessed with a space between each character  
def printLettersGuessed(arr):
    new_str = ""
    for i in arr:
        new_str += " " + i
    return new_str 

# Creates an array of dashes matching the length of the random word chosen
def convertToLines(word): 
    new_arr = []
    for i in word:
        new_arr.append("-")
    return new_arr

# Checks if the word is in the already guessed array of chars 
def alreadyGuessed(word, arr):
    for i in arr: 
        if word == i:
            return True
    return False

# Checks if the guessed char is in the word 
def guessInWord(guess, chosen):
    
    for i in chosen:
        if i == guess:
            return True
    return False

# Returns an array of indices of everywhere the guessed char is in the word
def getIndexes(guess, chosen): 
    arr = []
    for i in range (0, len(chosen)):
        if guess == chosen[i]:
            arr.append(i)
    return arr
            
# Prints the array of chars 
def printArr(arr):
    new_str = ""
    for i in arr:
        new_str += " " + i
    return new_str

# Converts mystery word array into a word by stripping it from the array into a string
def convertToWord(arr):
    new_str = ""
    for i in arr:
        new_str += i
    return new_str

# Decrypts the encrypted word by manipulating ASCII values 
def decrypt(ciphertext):
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if i % 2 == 0:
            plaintext += str(chr(ord(ciphertext[i]) - 1))
            
        else: 
            plaintext += str(chr(ord(ciphertext[i]) + 1))
        i += 1
    return plaintext

def main():
    # Chose random word
    words = ["WHDSPQZ" ,"XHO", "TTDBFRT", "QQJYF", "ENQD", "DNPK", "CNTR", "EHWHOD", "TSVMOHOF", "XNOCFQGTM"]
    wordToGuess = words[random.randint(0, len(words)-1)]
    
    # Set vars 
    lives = 10
    wordGuessCorrect = False
    lettersGuessed = []
    
    # wordToGuess_lines is an array that holds the guesses 
    wordToGuess_lines = convertToLines(wordToGuess)
    
    # Checks that we have more guess to give & we haven't guessed the correct word yet
    while (lives > 0 and wordGuessCorrect == False): 
        
        print("\n")
        print("You have " + str(lives) + " left and you have used these letters: " 
              + printLettersGuessed(lettersGuessed))
        print("Current word: " + printArr(wordToGuess_lines))
        guess = input("Guess a letter: ").upper()
        
        # If we already guessed the letter, we repeat the loop with no reprecussions 
        if (alreadyGuessed(guess, lettersGuessed)):
            print("You have already used that letter. Guess another letter.")
            
        else: 
            lettersGuessed.append(guess)
            
            # Checks if the guess is even in the word
            if (guessInWord(guess,wordToGuess)):    
                
                # If so, find all indices of its occurence 
                indexes = getIndexes(guess, wordToGuess)
                
                # Place guesses into the indices of occurence
                for i in indexes: 
                    wordToGuess_lines[i] = guess     
                    
            # If not in word, subtract a life
            else: 
                print("Your letter, " + guess + " is not in the word.")
                lives -= 1
        
        # Check if the wordToGuess is already guessed correctly 
        if convertToWord(wordToGuess_lines) == wordToGuess:
            wordGuessCorrect = True
       
    print("\n")
    
    # If word was guessed correctly, then enter this conditional
    if (wordGuessCorrect):
        print("Good Job! You guessed the word: " + wordToGuess)
        print("This was the encrypted message!")
        print("The decoded message says: " + decrypt(wordToGuess))
        
    # If we lost lives before we could guess correctly, enter this conditional
    else:
        print("You died. Sorry. The word was: " + wordToGuess)
        print("You'll have to guess the word correctly next time to decode the message!")
            
main()


