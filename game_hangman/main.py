import game_content 
import random

kraj = game_content.kraj
stolica = game_content.stolica
owoc = game_content.owoc

print("Zagrajmy w Wisielca!")
print("Dostępne są 3 kategorie:\n\t+ kraj\n\t+ stolica\n\t+ owoc")
print("Masz 5 szans na udzielenie poprawnej odpowiedzi.")
print("Możesz podać tylko 1 literę w danej próbie.")
print("Powodzenia!")

secret_word = ""
kategoria = input("Napisz, którą kategorię wybierasz: ")
if kategoria.upper() == "KRAJ":
    secret_word = random.choice(kraj).upper()
elif kategoria.upper() == "STOLICA":
    secret_word = random.choice(stolica).upper()
elif kategoria.upper() == "OWOC":
    secret_word = random.choice(owoc).upper()
else:
    print("Sorry, nie ma takiej kategorii.")
    exit()

expected_answer = list(secret_word)
hidden_word = list("_"*len(secret_word))

#print(secret_word)
if len(secret_word) > 4:
    print(f"{kategoria.upper()} NA {len(secret_word)} LITER: ")
else:
    print(f"{kategoria.upper()} NA {len(secret_word)} LITERY:")
#print(hidden_word)
#print(expected_answer)

user_letters = []
guess_number = 5
while guess_number > 0:
    print(f"Pozostałe szanse: {guess_number}")
    ask_user = (input("Podaj literę: "))
    user_guess = ask_user.upper()
    if user_guess not in user_letters:
        user_letters = user_letters + [user_guess]
#        print(user_letters)
    else:
        print("Ta litera została już użyta.")
        ask_user
        
    if len(user_guess) > 1:
        print(f"!!! Tylko jedna litera !!!\n{hidden_word}")
        user_letters.pop()
#        print(user_letters)
        ask_user
    else:
        if user_guess in expected_answer:
            for index, character in enumerate(expected_answer):
                if user_guess == character:
                    hidden_word[index] = character
            if hidden_word == expected_answer:
                print(f"\nZWYCIĘSTWO!!!\n{hidden_word}")
                print(game_content.wygrana)
                exit()
            else:
                print(f"\n\n{hidden_word}\nZgaduj dalej!")
        else:
            guess_number = guess_number - 1
            if guess_number == 4:
                print(game_content.glowa)
            elif guess_number == 3:
                print(game_content.reka_l)
            elif guess_number == 2:
                print(game_content.reka_p)
            elif guess_number == 1:
                print(game_content.noga_l)

else:
    print("GAME OVER")
    print(game_content.wisielec)
    print(f"Hasło: {secret_word}")


