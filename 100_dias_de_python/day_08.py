# functions with inputs
#arguments e parameters

def life_in_weeks(age):
    years_remaining = 90 - age
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12
    print(f"Você tem {days_remaining} dias, {weeks_remaining} semanas e {months_remaining} meses restantes.")
    
life_in_weeks(20)

def calculate_love_score(name1, name2):
    print("Welcome to the Love Calculator!")
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    true = t + r + u + e
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    love = l + o + v + e
    love_score = int(str(true) + str(love))
    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif love_score >= 40 and love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")
        
calculate_love_score("Rebeca", "Lucas")

def caesar_cipher(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter.isalpha():
            end_text += chr(ord(letter) + shift)
        else:
            end_text += letter
    print(f"The {direction}d text is {end_text}")
    
caesar_cipher("abc", 1, "encode")