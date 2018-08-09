import webapp2
from random import shuffle
import jinja2
import os
from random import randint
from Crypto.Cipher import XOR

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Uses XOR and a randomly generated KEY to encrypt message
def encrypt_message(message):
    key = ''
    for i in range(randint(1, 33)):
        key += str(randint(0,9))
    obj = XOR.new(key)
    ciphertext = obj.encrypt(message)
    cipher_dict = {
        'key': key,
        'ciphertext': ciphertext
    }
    
    return cipher_dict
    
# Uses XOR and given KEY to decrypt message
def decrypt_message(message, key):
    obj = XOR.new(key)
    decrypted_message = obj.decrypt(message)
    return decrypted_message

# First page seen by user, takes message input and POSTs to ResultPage
class WelcomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())

# Calls encrypt_message and displays a randomly generated KEY and encrypted message
class ResultPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/result.html')
        message = self.request.get("message")
        encrypted_dict = encrypt_message(message)
        self.response.write(about_template.render(encrypted_dict))
     
# Takes a message and KEY input and POSTs to DecryptResults   
class DecryptPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/decrypt.html')
        self.response.write(template.render())
    
# Results of a decryption from DecryptPage
class DecryptResults(webapp2.RequestHandler):
    def post(self):
        template = the_jinja_env.get_template('templates/decryptresult.html')
        message = self.request.get('message')
        key = self.request.get('key')
        message = decrypt_message(message, key)
        result_dict = {
            'message': message
        }
        self.response.write(template.render(result_dict))

    

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/result', ResultPage),
    ('/decrypt', DecryptPage),
    ('/decryptresult', DecryptResults)
    
], debug=True)