import random
class Generator:
    """Generates random text based on k-grams of an existing sample."""

    def __init__(self, source, n):
        """Construct a new generate using the source string and model of k-grams."""
        self._source = source
        self._order = n
        self._firstChar = self._source[:self._order] # First characters generated
        self._dictChar = {} # Dictionary to store generated characters
        self._dictChar[self._firstChar] = {}
        indexChar = self._source.find(self._firstChar) # Index of the first characters generated
        
        for char in self._source:
            # Adding the next characters to the dictionary
            if not self._source[indexChar+len(self._firstChar)] in self._dictChar[self._firstChar]:
                self._dictChar[self._firstChar][self._source[indexChar+len(self._firstChar)]] = 1
            else:
                self._dictChar[self._firstChar][self._source[indexChar+len(self._firstChar)]] += 1
            
            indexChar = self._source.find(self._firstChar, indexChar+len(self._firstChar)-1)
            if indexChar == -1:
                break
        
        self._currentChar = self._firstChar

    def nextChar(self):
        """Generate and return an additional character, given current state."""
        charValues = [val for val in self._dictChar[self._currentChar].values()] # List of characters' values
        randomChar = random.choices(list(self._dictChar[self._currentChar].keys()), weights=[(val/(sum(charValues))) for val in charValues])
        nextCharacter = self._currentChar[1:] + randomChar[0]
        
        if not nextCharacter in self._dictChar: # Checking if the next character isn't already in the dictionary
            self._currentChar = nextCharacter
            self._dictChar[self._currentChar] = {}
            indexCurChar = self._source.find(self._currentChar)
            
            if indexCurChar+len(self._currentChar) < len(self._source):
                # Adding generated characters in the dictionary
                for char in self._source:
                    if not self._source[indexCurChar+len(self._currentChar)] in self._dictChar[self._currentChar]:
                        self._dictChar[self._currentChar][self._source[indexCurChar+len(self._currentChar)]] = 1
                    else:
                        self._dictChar[self._currentChar][self._source[indexCurChar+len(self._currentChar)]] += 1
            
                    indexCurChar = self._source.find(self._currentChar, indexCurChar+len(self._currentChar)-1)
                    if indexCurChar == -1 or indexCurChar+len(self._currentChar) >= len(self._source): # When the program doesn't find the next character
                        break
            else:
                return '' # returning an empty string since it's at the end of the "source"
        
        return randomChar[0]