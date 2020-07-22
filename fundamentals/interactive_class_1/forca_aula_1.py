import random  #módulo para valores aleatórios
from word_list import words_list_gallows

def choice_word():
    word = random.choice(words_list_gallows)
    return word.upper()

print(choice_word())