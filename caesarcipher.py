#creating the caesar cipher class
class CaesarCipher:
    # constructor of the class for the encryption and decryption of the message 
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
    # using a for loop to iterate through the alphabet and using the % operator to wrap around the end of the alphabet
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self.__encoder = ''.join(encoder)
        self.__decoder = ''.join(decoder)
    # creating the encrypt and decrypt methods
    def encrypt(self, message):
        return self.__transform(message, self.__encoder)
    
    def decrypt(self, secret):
        return self.__transform(secret, self.__decoder)
    # creating the transform method to encrypt and decrypt the message 
    def __transform(self, original, code):  
        original = original.upper()
        msg = []
        for ch in original:  # encrypting letters only 
            if ch.isalpha():
                val = ord(ch) - ord('A')
                msg.append(code[val])
            else: # leaving non-letters unchanged   
                msg.append(ch)
        return ''.join(msg) 

# test case for the caesar cipher class:
cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)
