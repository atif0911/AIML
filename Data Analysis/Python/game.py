#a word is stored in a varviable and the user will input till he gets the word okay?
secretWord="sexy"
userGuess=""
guessCount=0
guessLimit=3
while guessCount!=guessLimit :
    print("Number of Guesses left: ",guessLimit-guessCount)
    userGuess=input("Enter ur guess: ")
    if userGuess == secretWord:
        print("U win")
        break
    guessCount+=1
if guessCount==guessLimit:
    print("U lost")