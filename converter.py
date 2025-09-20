from morse_data import morse_code_dict


class Morse:
    def __init__(self):
        self.morse_dict = morse_code_dict
        self.reverse_morse_dict = {value: key for key, value in morse_code_dict.items()}

    def encode(self, plain_text):
        encode_message = ""
        for letter in plain_text:
            encode_message += self.morse_dict[letter] + " "
        return encode_message

    def decode(self, morse_code):
        decoded_message = ''.join(self.reverse_morse_dict.get(code) for code in morse_code.split())
        return decoded_message



