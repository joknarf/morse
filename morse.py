# morse.py
# pylint: disable=missing-docstring

class Morse:
    MORSE_DECODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '/': ' '}

    def decode(self, message):
        letters = message.split(' ')
        if letters[0] == '':
            return ''
        decode_letters = [ self.MORSE_DECODE[l] for l in letters]
        print(''.join(decode_letters))
        return ''.join(decode_letters)
