word_list = ["carro", "borboleta", "arvore"]

import random

chosen_word = random.choice(word_list)

count_letters = len(chosen_word)
placeHolder = ""
for _ in range(count_letters):
    placeHolder += " _ "
    

print(placeHolder)
correct_letters = []
life = 6
game_over = False
while not game_over:
    guess = input("Escolha uma letra: ").lower()
    display = ""
    if guess not in chosen_word:
        life -= 1
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += " _ "
        
    print(display)
    
    if " _ " not in display:
        game_over = True
        print("Você venceu!")
    if life == 0:
        game_over = True
        print("Você perdeu!")
    