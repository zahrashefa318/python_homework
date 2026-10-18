#Task 4: Closure Practice---------------------------------------------------------------
def make_hangman(secret_word):
    guesses=[]

    def hangman_closure(letter):
        guesses.append(letter)
        answer=[]
        answer=[letter if letter in guesses else "_" for letter in secret_word]
        answer="".join(answer)
        print(answer)
        if answer==secret_word:
            return True
        else:
            return False

    return hangman_closure

def start_the_game():
    secret=input("Enter a secret word :")
    print("Game started, please enter one letter as guess ")
    sec=make_hangman(secret)
    guess=False
    
    while guess != True:
        user_input=input("Guess a letter:")
        guess=sec(user_input)

start_the_game()