# TODO: Import APIs (SHA256)
# Clean up CSS, make it look pretty

import webapp2
from random import shuffle
import jinja2
import os
from random import randint

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Dictionary for encryption: Key is in original message, value is in encoded message
# A1Z26 Encodes based on alphabet position; Difficult to decode since some replacements are multi-character; Will attempt workaround after MVP is completed
def encrypt_A1Z26(message):
    encrypt_dict = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26',
        ' ': ' ',
        ',': ',',
        '.': '.',
        '!': '!',
        '?': '?',
    }
    encrypted_str = ''
    for char in message:
        encrypted_str += encrypt_dict[char.lower()]
        encrypted_str += '-'
    return encrypted_str

#Ceasar encodes in a + or - 3; Each letter is encoded with it's value 3 after or before. A = D, B = E, etc.
def encrypt_caesar(message):
    encrypt_dict = {
        'a': 'd',
        'b': 'e',
        'c': 'f',
        'd': 'g',
        'e': 'h',
        'f': 'i',
        'g': 'j',
        'h': 'k',
        'i': 'l',
        'j': 'm',
        'k': 'n',
        'l': 'o',
        'm': 'p',
        'n': 'q',
        'o': 'r',
        'p': 's',
        'q': 't',
        'r': 'u',
        's': 'v',
        't': 'w',
        'u': 'x',
        'v': 'y',
        'w': 'z',
        'x': 'a',
        'y': 'b',
        'z': 'c',
        '.': '.',
        ',': ',',
        '!': '!',
        '?': '?',
        ' ': ' '
    }
    encrypted_str = ''
    for char in message:
        encrypted_str += encrypt_dict[char.lower()]
    return encrypted_str

def decrypt_caesar(message):
    decrypt_dict = {
        'd': 'a',
        'e': 'b',
        'f': 'c',
        'g': 'd',
        'h': 'e',
        'i': 'f',
        'j': 'g',
        'k': 'h',
        'l': 'i',
        'm': 'j',
        'n': 'k',
        'o': 'l',
        'p': 'm',
        'q': 'n',
        'r': 'o',
        's': 'p',
        't': 'q',
        'u': 'r',
        'v': 's',
        'w': 't',
        'x': 'u',
        'y': 'v',
        'z': 'w',
        'a': 'x',
        'b': 'y',
        'c': 'z',
        ' ': ' ',
        ',': ',',
        '!': '!',
        '.': '.',
        '?': '?'
        
    }
    decrypted_str = ''
    for char in message:
        decrypted_str += decrypt_dict[char]
    return decrypted_str

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())

class ResultPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/result.html')
        encrypted_message = self.request.get("message")
        encryption = self.request.get("encrypt")
        random_num = randint(1, 11)
        if encryption == "encrypt":
            for i in range(random_num):
                encrypted_message = encrypt_caesar(encrypted_message)
        encrypted_dict = {
            'encrypt_msg': encrypted_message,
            'randnum': random_num
        }
        self.response.write(about_template.render(encrypted_dict))
        
class DecryptPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Decryption page")
    def post(self):
        self.response.write("Decryption page POST")


app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/result', ResultPage),
    ('/decrypt', DecryptPage)
], debug=True)