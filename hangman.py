import random
import os


def word_selection():
    with open('data.txt', 'r', encoding='utf-8') as data:
        WORDS_DB = [x.strip().replace('á', 'a').replace('é', 'e').replace('í', 'i')
                        .replace('ó', 'o').replace('ú', 'u') for x in data]
        word = random.choice(WORDS_DB)
        return word       

#ASCII art for UI
HANGMAN = ('''\

        __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
        |  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
        |  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
        |   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
        |  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
        |__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
                                                                                        
        ''')
ERROR_0 = (''' 
  +---+
  |   |
      |
      |
      |
      |
=========

''')        
ERROR_1 = ('''
   +---+
  |   |
  O   |
      |
      |
      |
=========       
    ''')
ERROR_2 = ('''  
  +---+
  |   |
  O   |
  |   |
      |
      |
=========        
    ''')
ERROR_3 = ('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
ERROR_4 = (''' 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= ''')
ERROR_5 = (''' 
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= ''')
ERROR_6 = ('''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''')
WINNING_MESSAGE = ('''
____    ____  ______    __    __    ____    __    ____  ______   .__   __.    __   __   __  
\   \  /   / /  __  \  |  |  |  |   \   \  /  \  /   / /  __  \  |  \ |  |   |  | |  | |  | 
 \   \/   / |  |  |  | |  |  |  |    \   \/    \/   / |  |  |  | |   \|  |   |  | |  | |  | 
  \_    _/  |  |  |  | |  |  |  |     \            /  |  |  |  | |  . `  |   |  | |  | |  | 
    |  |    |  `--'  | |  `--'  |      \    /\    /   |  `--'  | |  |\   |   |__| |__| |__| 
    |__|     \______/   \______/        \__/  \__/     \______/  |__| \__|   (__) (__) (__) 
                                                                                           
''')
ERROR_LIST = (ERROR_0, ERROR_1, ERROR_2, ERROR_3, ERROR_4, ERROR_5, ERROR_6)


def run():
    #Welcome message
    print(HANGMAN)

    print('\n')
    print('Press 1 to start')
    print('Press 2 to exit')

    option = input('')
    assert option == '1' or option == '2', 'Select 1 or 2'
    if option == '2':
        exit()
    elif option == '1': 
        word = word_selection().upper()
        word_list = [x for x in word]
        under_scores = ['_'] * (len(word))
        mistakes = []

        random_word_dict = {}
        for id, letter in enumerate(word):
            if not random_word_dict.get(letter):
                random_word_dict[letter] = []
            random_word_dict[letter].append(id)

        counter = 0
        while '_' in under_scores and counter < 6:
        
            os.system("cls")
            print('\n' * 2)    
            for character in under_scores:
                print(character + ' ', end = '')
            print('\n')     
            print(ERROR_LIST[counter])
            print(*mistakes, sep = ',')    
            choosen_letter = input('Try a letter: ').strip().upper()
            assert choosen_letter.isalpha(), "You can only use letters"
            
            if choosen_letter in word_list:
                for id in random_word_dict[choosen_letter]:
                    under_scores[id] = choosen_letter
            else:
                mistakes.append(choosen_letter)
                counter += 1

            if '_' not in under_scores:
                os.system("cls")
                print(WINNING_MESSAGE)
                print('The secret word is' + ' ' + word)
                try_again = input('Do you want to try again? [y/n]: ')
                assert try_again == 'y' or try_again == 'n', 'Select y or n'
                if try_again == 'y':
                    os.system("cls")
                    run()
                else:
                    exit()

        if counter == 6:
            os.system("cls")
            print(ERROR_LIST[counter])
            print('You lose, the secret word was:' + ' ' + word)
            try_again = input('Do you want to try again? [y/n]: ')
            assert try_again == 'y' or try_again == 'n', 'Select y or n'
            if try_again == 'y':
                os.system("cls")
                run()
            else:
                exit()    
                     

if __name__ == '__main__':
    run()
    
       