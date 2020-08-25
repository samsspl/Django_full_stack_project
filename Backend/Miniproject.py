import random
# Guess from user
def userGuess():
    return list(input("What is your guess?"))

# Generate random 3 digits
def generate_digits():
    digits = [str(num) for num in range(10)]

    #shuffle the generate_digits
    random.shuffle(digits)
    #take the first 3 digits 
    return digits[:3]

# Generate clues for user
def generateClue(code,userGuess):
    if userGuess == code:
        return "code Cracked"
    
    clues = []

    for count,num in enumerate(userGuess):
        if(num == code[count]):
            clues.append("match")
        elif num in code:
            clues.append("close")
        
    if clues == []:
        return ["nope"]
    else:   
        return clues


# Game loop

print("Welcome Code Breaker!")

secrets = generate_digits()

clue_report = []

while clue_report != "Code Cracked":
    guess = userGuess()

    clue_report = generateClue(guess,secrets)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
