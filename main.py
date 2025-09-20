from converter import Morse

morse = Morse()

end_converting = False

while not end_converting:
    mode = input("Do you want to encode or decode? e/d) >> ").lower()

    if mode == "e":
        text = input("Please write the text you want to encode >> ").lower()
        print(morse.encode(text))
    elif mode == "d":
        morse_code = input("Please write the morse code you want to decode >> ")
        print(morse.decode(morse_code))
    else:
        print("Invalid option. Please choose 'e' or 'd'.")

    keep_converting = input("Do you want to continue? (y/n) ").lower()
    if keep_converting == "y":
        end_converting = False
    elif keep_converting == "n":
        end_converting = True
        print("Bye. Come back soon!")
    else:
        print("Invalid option. Please choose 'y' or 'n'.")


