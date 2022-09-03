def caesar(direction, message, key):
    final_output = ""
    alphabet_lgth = len(alphabet)-1
    for char in message:
        if char in alphabet:
            base_char_index = alphabet.index(char)
#            print(f"Base char: {char} is on the position: {base_char_index}.")
            if direction == "encrypt":
                new_char_index = base_char_index + key
                if new_char_index <= alphabet_lgth:
                    final_output += alphabet[new_char_index]
                else:
                    char_over_alph = (new_char_index % alphabet_lgth)-1
                    final_output =  final_output + alphabet[char_over_alph]
            elif direction == "decrypt":
                new_char_index = base_char_index - key
                if new_char_index >= 0:
                    final_output += alphabet[new_char_index]
                else:
                    char_before_0 = (new_char_index % alphabet_lgth)+1
                    final_output += alphabet[char_before_0]
        else:
            final_output = final_output + char

    print(f"Your message: {final_output}")

alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
           'p', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż', ' ', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '0', '.', ',', '!', '?', ':', '-', '+', '%']

directions = ['encrypt', 'decrypt']

direction = (input("Do you want to encrypt or decrypt message? ")).lower()
if direction in directions:
    user_message = (input("Write your message here:\n")).lower()
    user_key = int(input("Write key lenght:\n"))
    caesar(direction, user_message, user_key)
else:
    print("Unknown command.")
    exit()
