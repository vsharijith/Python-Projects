import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

hollywood = ["inception", "avatar", "the dark knight", "pulp fiction", "fight club",
    "the godfather", "forrest gump", "the shawshank redemption", "titanic", "jurassic park",
    "the matrix", "gladiator", "interstellar", "the avengers", "star wars",
    "the lord of the rings", "back to the future", "saving private ryan", "braveheart", "schindler's list"]

bollywood = ["sholay", "dilwale dulhania le jayenge", "lagaan", "3 idiots", "rang de basanti",
    "dangal", "queen", "kahaani", "gully boy", "taare zameen par",
    "piku", "barfi", "masaan", "pink", "andhadhun",
    "bajrangi bhaijaan", "udta punjab", "zindagi na milegi dobara", "swades", "chak de india"]

mollywood = ["drishyam", "premam", "bangalore days", "kumbalangi nights", "lucifer",
    "thanmathra", "anjam pathiraa", "charlie", "ee ma yau", "ayanum",
    "jallikattu", "android kunjappan ver 5.25", "traffic", "udaan", "virus",
    "north 24 kaatham", "njan prakashan", "angamaly diaries", "maheshinte prathikaaram", "thondimuthalum driksakshiyum"]

np = ["corbett", "kaziranga", "kanha", "bandhavgarh", "ranthambore",
    "sundarbans", "gir", "periyar", "manas", "satpura",
    "bandipur", "dudhwa", "nagarhole", "pench", "sanctuary",
    "sariska", "valley of flowers", "ghatigaon", "mudumalai", "silent valley"]

pm = ["jawaharlal nehru", "lal bahadur shastri", "indira gandhi", "morarji desai",
    "charan singh", "rajiv gandhi", "vishwanath pratap singh", "chandra shekhar",
    "pv narasimha rao", "atal bihari vajpayee", "h d deve gowda", "i k gujral",
    "manmohan singh", "narendra modi"]

president = ["rajendra prasad", "sarvepalli radhakrishnan", "zakir husain", "vv giri",
    "fakhruddin ali ahmed", "neelam sanjiva reddy", "gyani zail singh", "r venkataraman",
    "shankar dayal sharma", "k r narayanan", "a p j abdul kalam", "pratibha patil",
    "pranab mukherjee", "ram nath kovind", "droupadi murmu"]

category = [president,pm,np,hollywood,mollywood,bollywood]
x = random.choice(category)

print(logo)

print("Welcome to Hangman.\nYou have 6 lives to guess each letter. Life decreases as you guess the wrong letter.\n\n")

if x == hollywood:
    print("Guess the Hollywood Film!\n*spaces and special characters can be used*")
elif x == bollywood:
    print("Guess the Bollywood Film!\n*spaces and special characters can be used*")
elif x == mollywood:
    print("Guess the Mollywood Film!\n*spaces and special characters can be used*")
elif x == np:
    print("Guess the National Park in India!\n*spaces and special characters can be used*")
elif x == president:
    print("Guess the President!\n*spaces and special characters can be used*")
else:
    print("Guess the Prime Minister of India!\n*spaces and special characters can be used*")

word_list = x


chosen_word = random.choice(word_list)
#print(chosen_word)

underscore = ""
for position in range(len(chosen_word)):
    underscore += "_"
print(underscore)
game_over = False
correct_letter = []

print(stages[6])

letters_attempted = []

while game_over == False:
    guess_word = input("Guess a letter\n").lower()

    wrong = ""
    display = ""

    for letter in chosen_word:
        if letter == guess_word:
            display += letter
            correct_letter.append(guess_word)
        elif letter in correct_letter:
            display += letter
        elif letter != guess_word:
            display += "_"
            wrong += guess_word


    print(display)

    if guess_word not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("You Win")

    print(stages[lives])

    #
    letters_attempted.append(guess_word)
    print(f"Letters attepmted are {letters_attempted}")

print('The word is "'+ chosen_word +'"')