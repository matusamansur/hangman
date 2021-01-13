import random

listOfWords = ["arara", "python"]
# mistakes = 0
# word = random.choice(listOfWords).lower()
# secret = list("_"*len(word))

def drawMistakes():
    if mistakes == 1:
        print("O")
    elif mistakes == 2:
        print("O")
        print("|")
    elif mistakes == 3:
        print(" O")
        print("/", end = '')
        print("|")
    elif mistakes == 4:
        print(" O")
        print("/", end = '')
        print("|", end = '')
        print("\\")
    elif mistakes == 5:
        print(" O")
        print("/", end = '')
        print("|", end = '')
        print("\\")
        print("/")
    elif mistakes == 6:
        print(" O")
        print("/", end = '')
        print("|", end = '')
        print("\\")
        print("/", end = ' ')
        print("\\")

while True:
    mistakes = 0
    word = random.choice(listOfWords).lower()
    secret = list("_"*len(word))
    
    while True:
        print("Guess a Letter: " + " ".join(secret))
        letter = input().lower()

        indexOfGuessed = [i for i, ltr in enumerate(word) if ltr == letter]
        if(indexOfGuessed):
            for i in indexOfGuessed:
                secret[i] = letter
        else:
            mistakes+=1
            if (mistakes!=6):
                drawMistakes()
                print("Uh oh! Try Again.") 

            else:
                print("You lost! The word was {}".format(word))
                drawMistakes()
                break
            
        if(not "_" in secret):
            print("Congratz! You Won! The word was: {}".format(word))       
            break

    opt = input("Press (1) to play again or (0) to exit the program: ")
    if(opt == '0'):
        print("Exiting...")
        exit(0)
        
