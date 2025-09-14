import random


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

secret_word_list = ["understanding", "traditional", "switch", "case", "statements", 
                    "godzilla", "adventure", "noodles", "idiot", "barbeque", "apple", 
                    "fruit", "fridge", "television", "skin", "languages", "interesting",
                    "platinum", "stupid", "hello", "drawing", "cat", "dog", "google", 
                    "strawberry", "blueberry", "history", "beach", "musuem", "intelligence",
                    "regulations", "fitness", "hatred", "magic", "wizard", "books", "phobias",
                    "Cornmeal", "donate", "charity", "initiation", "japan", "cambodia", "education",
                    "appreciation", "organisation", "anime", "cartoon", "movies", "programming", 
                    "banana", "mathematics", "nature", "ultraanatomy", "toxicomorphology", 
                    "electroentomonomy", "mineralobiomorphology", "parageography", "neurohistory", 
                    "pararadiogenics", "gold", "formula", "range", "heart", "assignment", "alphabet",
                    "operate", "tremor", "poise", "plutonium", "unvarying", "yoga", "amiable", "scribing", 
                    "fructose", "clever", "protract", "glacial", "delouse", "glimmer", "antirust", "judo",
                    "unsorted", "diaper", "almanac", "trilogy", "secrecy", "unloved", "velvet", "asparagus",
                    "phonics", "lilly", "stoppage", "lego", "penalty", "senator", "ripeness", "greedily",
                    "pluck", "undusted", "bauble", "serve", "moocher", "sizzle", "sponge", "eject", "conform",
                    "evident", "atop", "shrine", "cinch", "nemeses", "thespian", "grief", "bullpen", "amendable",
                    "catching", "wind", "dumping", "daunting", "munchkin", "yippee", "mortified", "pavilion",
                    "dating", "afloat", "armband", "trimness", "victory", "irregular", "sandpaper", "ascend",
                    "negate", "upstroke", "traps", "pajamas", "violation", "snugness", "italicize", "stank",
                    "doorman", "hardhead", "duffel", "aged", "pucker", "outhouse", "absently", "tribune",
                    "backup", "fascism", "stinky", "willing", "available", "cornbread", "purifier", "angular"]

r = random.randint(0, len(secret_word_list) - 1)
secret_word = secret_word_list[r]

masked_word = [ '_' ] * len(secret_word)
# list to store incorrect guess
wrong_char_list = []  

num_attempts = 0


if __name__ == '__main__':
    while num_attempts < 6:
        matched_letter = False
        # display the hangman body
        print(hangman[num_attempts])
        # display the space in the underscore
        print(" ".join(masked_word), '\n')

        print(f"Wrong letter: {', '.join(wrong_char_list)}")

        guess_letter = input("Guess a letter: ")

        # validate that user input is alphabetic chararcters
        if not guess_letter.isalpha():
            print("\nPlease enter a letter from A to Z.")
            continue

        for index, char in enumerate(secret_word):
            if guess_letter == char:
                masked_word[index] = char.capitalize()
                matched_letter = True
        
        # increase the attempt if guess character is incorrect
        if matched_letter == False:
            if not guess_letter in wrong_char_list:
                num_attempts += 1
                wrong_char_list.append(guess_letter)
            else:
                print("You already entered that letter!")

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

