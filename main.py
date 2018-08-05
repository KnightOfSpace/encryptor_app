

def encrypt_A1Z26(message):
    encrypted_str = ''
    for char in message:
        if char.lower() == 'a':
            encrypted_str += '1'
        elif char.lower() == 'b':
            encrypted_str += '2'
        elif char.lower() == 'c':
            encrypted_str += '3'
        elif char.lower() == 'd':
            encrypted_str += '4'
        elif char.lower() == 'e':
            encrypted_str += '5'
        elif char.lower() == 'f':
            encrypted_str += '6'
        elif char.lower() == 'g':
            encrypted_str += '7' #No idea why an error is showing up here, code runs fine.
        elif char.lower() == 'h':
            encrypted_str += '8'
        else:
            encrypted_str += char
            
    return encrypted_str

print encrypt_A1Z26("gg nerd")