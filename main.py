from tkinter import *
from converter import Morse

DARK_GREEN = "#064232"
DARK_CYAN = "#568F87"
ROSE_WHITE = "#FFF5F2"
PALE_ROSE = "#F5BABB"
FONT_NAME = "Courier"

window = Tk()
window.title("Text ↔ Morse Converter")
window.config(padx=50, pady=50, background=DARK_CYAN)

# Labels
title_label = Label(text="MORSE CODE CONVERTER", fg=DARK_GREEN, bg=DARK_CYAN, font=(FONT_NAME, 15, "bold"))
title_label.grid(column=1, row=0, pady=(0, 30))

# Radiobuttons
radio_state = IntVar()
text_radio = Radiobutton(text="Convert Text to Morse Code", value=1, variable=radio_state, fg=DARK_GREEN,
                         bg=DARK_CYAN, font=(FONT_NAME, 15))
morse_radio = Radiobutton(text="Convert Morse Code to Text", value=2, variable=radio_state, fg=DARK_GREEN,
                          bg=DARK_CYAN, font=(FONT_NAME, 15))
text_radio.grid(column=0, row=1)
morse_radio.grid(column=0, row=2, pady=(0, 25))

# Text Boxes
text_box1 = Text(width=40, height=5)
text_box1.grid(column=0, row=3)

text_box2 = Text(width=40, height=6)
text_box2.grid(column=2, row=3)

# Button
convert_button = Button(text="Convert", bg=PALE_ROSE, fg=DARK_GREEN, height=2, width=15, font=(FONT_NAME, 10, "bold"))
convert_button.grid(column=1, row=3)

window.mainloop()


# morse = Morse()

# end_converting = False
# while not end_converting:
#     mode = input("Do you want to encode or decode? (e/d) >> ").lower()
#
#     if mode == "e":
#         text = input("Please write the text you want to encode >> ").lower()
#         print(morse.encode(text))
#     elif mode == "d":
#         morse_code = input("Please write the morse code you want to decode >> ")
#         print(morse.decode(morse_code))
#     else:
#         print("Invalid option. Please choose 'e' or 'd'.")
#
#     keep_converting = input("Do you want to continue? (y/n) ").lower()
#     if keep_converting == "y":
#         end_converting = False
#     elif keep_converting == "n":
#         end_converting = True
#         print("Bye. Come back soon!")
#     else:
#         print("Invalid option. Please choose 'y' or 'n'.")


