from morse_data import MORSE_CODE_DICT


class Morse:
    def __init__(self):
        self.morse_dict = MORSE_CODE_DICT
        self.reverse_morse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}

    def encode(self, plain_text):
        """
        Convert plain text into Morse code.
        Unknown characters get printed.
        """
        try:
            encode_message = []
            for letter in plain_text:
                encode_message.append(self.morse_dict[letter])
            return " ".join(encode_message)
        except KeyError as error_message:
            return f"The {error_message} is not supported. Please choose something else."

    def decode(self, morse_code):
        """
        Convert Morse code into plain text.
        Unknown Morse symbols are replaced with '?'.
        """
        decoded_message = ''.join(self.reverse_morse_dict.get(code, "?") for code in morse_code.split())
        return decoded_message



