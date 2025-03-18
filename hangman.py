hangman = [ '''
      _______
     |/      |
     |      
     |
     |
     |
     |
    _|___
''','''
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___
''','''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |
     |
    _|___
''','''
      _______
     |/      |
     |      (_)
     |      \\|
     |       |
     |
     |
    _|___
''', '''
      _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |
     |
    _|___
''','''
      _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / 
     |
    _|___
''',
'''
      _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / \\
     |
    _|___
''']

secret_word = "godzilla"

masked_word = [ '_' ] * len(secret_word)
# list to store incorrect guess
wrong_char_list = []  

num_attempts = 0

while num_attempts < 6:
    matched_letter = False

    # display the hangman body
    print(hangman[num_attempts])
    # display the space in the underscore
    print(" ".join(masked_word), '\n')
    print(f"Wrong letter: {', '.join(wrong_char_list)}")
    guess_letter = input("Guess a letter: ")

    for index, char in enumerate(secret_word):
        if guess_letter == char:
            masked_word[index] = char.capitalize()
            matched_letter = True
    
    # increase the attempt if guess character is incorrect
    if matched_letter == False:
        num_attempts += 1
        wrong_char_list.append(guess_letter)

    # check if the words is already completed
    if not '_' in masked_word:
        print(hangman[num_attempts])
        # display the space in the underscore
        print(" ".join(masked_word), '\n')
        print(f"Yipee you won! The word is '{secret_word}'.")
        break

if num_attempts == 6:
    print(hangman[num_attempts])
    print(f"\nSorry you lose! :( the word was {secret_word}")