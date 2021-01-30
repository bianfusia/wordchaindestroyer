import requests

import random

from art import *

 

url  = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json'

 

resp = requests.get(url=url)

 

data = resp.json()

word_list = []

keep_list = []

for key in data:

    if len(key) > 2:

        word_list.append(key)

 

def get_word(start_letter,con_letter,no_word):
    
    global keep_list
    man_list = keep_list.copy()

    man_list = list(filter(lambda x: (len(x) >= no_word), man_list))

    man_list = list(filter(lambda x : (x[0] == start_letter), man_list))

    man_list = list(filter(lambda x: (con_letter in x), man_list))

    full_int = len(man_list)-1

    if full_int < 0:
        return print("\n" + "no available words detected" + "\n")

    rand_word = (random.randint(0,full_int))
    chosen_word = man_list[rand_word]
    keep_list.remove(chosen_word)

    print("\n" + man_list.pop(rand_word) + "\n")
        


def get_last(start_letter, last_letter):

    global keep_list
    man_list = keep_list.copy()
    
    man_list = list(filter(lambda x: (last_letter == x[-1]), man_list))
    man_list = list(filter(lambda x: (len(x) >= 10), man_list))
    man_list = list(filter(lambda x : (x[0] == start_letter), man_list))
    man_list = list(filter(lambda x: (con_letter in x), man_list))

    full_int = len(man_list)-1

    if full_int < 0:
        man_list = keep_list.copy()
        man_list = list(filter(lambda x : (x[0] == start_letter), man_list))
        man_list = list(filter(lambda x: (len(x) >= 10), man_list))
        man_list = list(filter(lambda x: (con_letter in x), man_list))
        full_int = len(man_list)-1
        rand_word = (random.randint(0,full_int))
        chosen_word = man_list[rand_word]
        keep_list.remove(chosen_word)
        print("\n" + man_list.pop(rand_word)+ "\n")
    
    else:

        full_int = len(man_list)-1
        rand_word = (random.randint(0,full_int))
        chosen_word = man_list[rand_word]
        keep_list.remove(chosen_word)
        print("\n" + man_list.pop(rand_word) + "\n")

def ded_last(start_letter, last_letter, con_letter, no_word):

    global keep_list
    man_list = keep_list.copy()
    
    man_list = list(filter(lambda x: (last_letter == x[-1]), man_list))
    man_list = list(filter(lambda x: (len(x) >= no_word), man_list))
    man_list = list(filter(lambda x : (x[0] == start_letter), man_list))

    full_int = len(man_list)-1

    if full_int < 0:
        man_list = keep_list.copy()
        man_list = list(filter(lambda x : (x[0] == start_letter), man_list))
        man_list = list(filter(lambda x: (len(x) >= no_word), man_list))
        full_int = len(man_list)-1
        rand_word = (random.randint(0,full_int))
        chosen_word = man_list[rand_word]
        keep_list.remove(chosen_word)
        print("\n" + man_list.pop(rand_word)+ "\n")
    
    else:

        full_int = len(man_list)-1
        rand_word = (random.randint(0,full_int))
        chosen_word = man_list[rand_word]
        keep_list.remove(chosen_word)
        print("\n" + man_list.pop(rand_word) + "\n")

print(text2art('''On9
Word Chain
DESTROYER''', font="small"))

print("developed by: @beeeatant")
   

while True:

    keep_list = word_list.copy()

    choice = int(input("\n" + "1: required letter\n2: hard mode\n3: deathtorl\nPlease choose a mode:"))

    while True:
        if choice == 1:

            print("\n" + "Key 1 at the start letter to end game \n")

            start_letter = str(input("key in the start letter: "))
            
            if start_letter == "1":
                break

            con_letter = str(input("key in the contain letter: "))

            no_word = int(input("number of words: "))

            get_word(start_letter,con_letter,no_word)

        elif choice == 2:

            print("\n" + "Key 1 at the start letter to end game")
            last_letter = str(input("key in the ending letter: "))

            while True:

                start_letter = str(input("\n" + "key in the start letter: "))
                if start_letter == "1":
                    break
                get_last(start_letter, last_letter)

        elif choice == 3:

            print("\n" + "Key 1 at the start letter to end game")
            last_letter = str(input("How friendly do you want to be?: "))

            while True:

                start_letter = str(input("\n" + "key in the start letter: "))
                con_letter = str(input("\n" + "key in the containing letter: "))
                no_word = int(input("number of words: "))
                if start_letter == "1":
                    break
                ded_last(start_letter, last_letter,con_letter,no_word)

            break
