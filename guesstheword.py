# Displaying the initial message to the user
print("GUESS THE WORD ! Good Luck")

# The word that needs to be guessed
word = "STRING"

# Creating a list to hold the letters of the word
guess_word = []

# Adding each character of the word to the guess_word list
for i in word:
    guess_word.append(i) 

# Creating a list with underscores to represent each letter in the word initially
guessed_word = ["_"] * len(word)

# Loop runs until the player guesses the whole word correctly
while guess_word != guessed_word:
    # Asking the user to input a letter and converting it to uppercase
    user_input = input("Enter the letter in word: ").upper()

    # Checking if the guessed letter is in the word
    if user_input in guess_word:
        # If the letter is correct, update the guessed_word list at the corresponding index
        guessed_word[guess_word.index(user_input)] = user_input
        print("Correct Guess\n! ")
        print(guessed_word)  # Displaying the partially guessed word
    else:
        # If the guess is incorrect, notify the user
        print("wrong guess! try again\n")
        
# When the word is fully guessed, congratulate the player
print("Congratulations!")
