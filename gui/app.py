from tkinter import *
from tkinter import messagebox
from converter import Morse

DARK_GREEN = "#064232"
DARK_CYAN = "#568F87"
ROSE_WHITE = "#FFF5F2"
PALE_ROSE = "#F5BABB"
FONT_NAME = "Courier"


class MorseApp:
    def __init__(self, window):
        self.morse = Morse()

        window.title("Text ↔ Morse Converter")
        window.config(padx=50, pady=50, background=DARK_CYAN)

        # Labels
        title_label = Label(text="MORSE CODE CONVERTER",
                            fg=DARK_GREEN, bg=DARK_CYAN,
                            font=(FONT_NAME, 15, "bold"))
        title_label.grid(column=1, row=0, pady=(0, 30))

        # Radiobuttons
        self.radio_state = IntVar(value=1)
        text_radio = Radiobutton(text="Convert Text to Morse Code",
                                 value=1, variable=self.radio_state,
                                 fg=DARK_GREEN,
                                 bg=DARK_CYAN, font=(FONT_NAME, 15),
                                 command=self.clear_input)
        morse_radio = Radiobutton(text="Convert Morse Code to Text",
                                  value=2, variable=self.radio_state,
                                  fg=DARK_GREEN,
                                  bg=DARK_CYAN, font=(FONT_NAME, 15),
                                  command=self.clear_input)
        text_radio.grid(column=0, row=1)
        morse_radio.grid(column=0, row=2, pady=(0, 25))

        # Text Boxes
        self.text_box1 = Text(width=40, height=5)
        self.text_box1.insert(END, "Enter what you wish to convert: ")
        self.text_box1.grid(column=0, row=3)
        self.text_box1.bind("<FocusIn>", self.clear_placeholder)

        self.text_box2 = Text(width=40, height=6, state="disabled")
        self.text_box2.grid(column=2, row=3)

        # Button
        convert_button = Button(text="Convert",
                                bg=PALE_ROSE,
                                fg=DARK_GREEN,
                                height=2, width=15,
                                font=(FONT_NAME, 11, "bold"),
                                command=self.convert)
        convert_button.grid(column=1, row=3)

    def convert(self):
        if self.text_box1.get("1.0", END).strip() != "Enter what you wish to convert:":
            choice = self.radio_state.get()
            input_value = self.text_box1.get("1.0", END).strip()

            if choice == 1 and not self.is_morse(input_value):
                result = self.morse.encode(input_value.lower())
            elif choice == 2 and self.is_morse(input_value):
                result = self.morse.decode(input_value)
            else:
                messagebox.showwarning("Conversion Error", "Please choose the right converter.")
                return

            self.text_box2.config(state="normal")
            self.text_box2.delete("1.0", END)
            self.text_box2.insert(END, result)
            self.text_box2.config(state="disabled")

    def clear_placeholder(self, event):
        if self.text_box1.get("1.0", END).strip() == "Enter what you wish to convert:":
            self.text_box1.delete("1.0", END)

    def clear_input(self):
        if self.text_box1.get("1.0", END).strip() != "Enter what you wish to convert:":
            self.text_box1.delete("1.0", END)
            self.text_box2.config(state="normal")
            self.text_box2.delete("1.0", END)
            self.text_box2.config(state="disabled")

    def is_morse(self, input_value):
        morse_chars = {".", "-", " ", "/"}
        for char in input_value:
            if char not in morse_chars:
                return False
        return True
