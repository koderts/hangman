from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

HANGMAN_PICS = [r'''
      _______
     |/      |
     |
     |
     |
     |
     |
    _|___
''',r'''
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___
''',r'''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |
     |
    _|___
''',r'''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |
     |
    _|___
''', r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
    _|___
''',r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
''',
r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
''']

SECRET_WORD_LIST = ["understanding", "traditional", "switch", "case", "statements", "godzilla", "adventure", "noodles", "idiot", "barbeque", "apple", "fruit", "fridge", "television", "skin", "languages", "interesting", "platinum", "stupid", "hello", "drawing", "cat", "dog", "google", "strawberry", "blueberry", "history", "beach", "musuem", "intelligence", "regulations", "fitness", "hatred", "magic", "wizard", "books", "phobias", "Cornmeal", "donate", "charity", "initiation", "japan", "cambodia", "education", "appreciaition", "organisation", "anime", "cartoon", "movies", "programming", "banana", "mathematics", "nature", "ultraanatomy", "toxicomorphology", "electroentomonomy", "mineralobiomorphology", "parageography", "neurohistory", "pararadiogenics", "gold", "formula", "range", "heart", "assignment", "alphabet"]

def start_new_game():
    session['secret_word'] = random.choice(SECRET_WORD_LIST)
    session['masked_word'] = [ '_' ] * len(session['secret_word'])
    session['wrong_char_list'] = []
    session['num_attempts'] = 0
    session['message'] = ""
    session['game_over'] = False

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'secret_word' not in session or request.form.get('new_game'):
        start_new_game()

    if request.method == 'POST' and not session.get('game_over'):
        guess_letter = request.form.get('guess', '').lower()
        session['message'] = ""

        if not guess_letter.isalpha() or len(guess_letter) != 1:
            session['message'] = "Please enter a single letter from A to Z."
        elif guess_letter in session['wrong_char_list'] or guess_letter.upper() in session['masked_word']:
            session['message'] = "You already entered that letter!"
        else:
            matched_letter = False
            masked_word_list = session['masked_word']
            for index, char in enumerate(session['secret_word']):
                if guess_letter == char:
                    masked_word_list[index] = char.upper()
                    matched_letter = True
            
            session['masked_word'] = masked_word_list

            if not matched_letter:
                session['num_attempts'] += 1
                session['wrong_char_list'].append(guess_letter)

        if '_' not in session['masked_word']:
            session['message'] = f"Yipee you won! The word is '{session['secret_word']}'."
            session['game_over'] = True
        elif session['num_attempts'] >= 6:
            session['message'] = f"Sorry you lose! :( The word was '{session['secret_word']}'."
            session['game_over'] = True
    
    # Ensure these keys exist in the session
    masked_word_display = " ".join(session.get('masked_word', []))
    wrong_letters_display = ", ".join(session.get('wrong_char_list', []))
    hangman_pic = HANGMAN_PICS[session.get('num_attempts', 0)] if session.get('num_attempts', 0) < len(HANGMAN_PICS) else HANGMAN_PICS[-1]


    return render_template('index.html', 
                           hangman_pic=hangman_pic,
                           masked_word=masked_word_display,
                           wrong_letters=wrong_letters_display,
                           message=session.get('message', ''),
                           game_over=session.get('game_over', False))

if __name__ == '__main__':
    app.run(debug=True)
