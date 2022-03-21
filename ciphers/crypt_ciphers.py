import math 

class CeaserCipher(object):

    def __init__(self, message) -> None:
        
        SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.-_;:/()'"
        
        self.SYMBOLS = SYMBOLS
        self.message = message

    def encrypt_message(self, key):

        translated = ''

        for symbol in self.message:
    
            if symbol in self.SYMBOLS:
                
                num = self.SYMBOLS.find(symbol)
            
                num = num + int(key)

                if num >= len(self.SYMBOLS):
                    
                    num = num - len(self.SYMBOLS)
                    
                elif num < 0:
                    
                    num = num + len(self.SYMBOLS)
                
                translated = translated + self.SYMBOLS[num]
            
            else:

                translated = translated + symbol

        return translated

    def decrypt_message(self, key):

        translated = ''

        for symbol in self.message:
    
            if symbol in self.SYMBOLS:
                
                num = self.SYMBOLS.find(symbol)
            
                num = num - int(key)
                    
                if num >= len(self.SYMBOLS):
                    
                    num = num - len(self.SYMBOLS)
                    
                elif num < 0:
                    
                    num = num + len(self.SYMBOLS)
                
                translated = translated + self.SYMBOLS[num]
            
            else:

                translated = translated + symbol

        return translated

class TranspositionalCipher(object):

    def __init__(self, message) -> None:
        
        self.message =message

    def encrypt_message(self, key):

        ciphertext = [''] * int(key)

        for column in range(key):
    
            currentIndex = column

            while currentIndex < len(self.message):

                ciphertext[column] += self.message[currentIndex]

                currentIndex += key

        return ''.join(ciphertext)

    def decrypt_message(self, key):

        numOfColumns = int(math.ceil(len(self.message) / float(key)))

        numOfRows = int(key)

        numOfShadedBoxes = (numOfColumns * numOfRows) - int(len(self.message))

        plaintext = [''] * numOfColumns

        column = 0

        row = 0

        for symbol in self.message:
            
            plaintext[column] += symbol

            column += 1

            if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):

                column = 0

                row += 1

        plaintext = ''.join(plaintext)

        return plaintext