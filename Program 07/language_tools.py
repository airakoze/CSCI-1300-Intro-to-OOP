import string
class LanguageHelper:
    def __init__(self, words):
        """
        Class constructor responsible for recording all words from the language into an internal 
        data representation, and stripping any extraneous whitespace from each entry 
        (such as newline characters that will appear in a file)
        """
        setWords = set()
        
        for word in words:
            word.strip() # Removing any leading or trailing whitepace
            
            if '\n' in word:
                word.rstrip('\n') # Removes any new line character
            
            setWords.add(word)
        
        self._words = setWords
    
    def __contains__(self,query):
        """
        The method determine whether the string is considered a legitimate word
        returning True if the word is contained in the language and False otherwise.
        """
        if query in self._words:
            return True
        else:
            return False
        
    def getSuggestions(self,query):
        """
        The method will return a sorted list of suggestions of words in the language
        """
        lowerLetters = string.ascii_lowercase
        upperLetters = string.ascii_uppercase
        suggestions = []
        
        # Changing letters if the first letter is uppercase
        if query[0].isupper():
            newList = set()
            for word in self._words:
                newList.add(word.capitalize())
            self._words = newList

        if query in self._words:
            suggestions.append(query)
        else:
            # Removing one character
            for k in range(len(query)):
                newQuery = list(query)
                newQuery.pop(k) 
                if ''.join(newQuery) in self._words and not (''.join(newQuery) in suggestions):
                    suggestions.append(''.join(newQuery))
            
            # Inverting two neighboring characters
            for j in range(len(query) - 1):
                newQuery = list(query)
                nextCharacter = newQuery[j+1]
                newQuery[j+1] = newQuery[j]
                newQuery[j] = nextCharacter
                if ''.join(newQuery) in self._words and not (''.join(newQuery) in suggestions):
                    suggestions.append(''.join(newQuery))
            
            # Adding a lowercase letter to the query
            for l in range(len(query)):
                newQuery = list(query)
                for k in range(len(lowerLetters)):
                    newQuery = list(query)
                    newQuery.insert(l, lowerLetters[k])
                    if ''.join(newQuery) in self._words and not (''.join(newQuery) in suggestions):
                        suggestions.append(''.join(newQuery))
            

            # Changing one character
            for k in range(len(query)):
                newQuery = list(query)
                for m in range(len(upperLetters)):
                    newQuery = list(query)
                    # Changing the first Uppercase letter
                    if newQuery[0].isupper():
                        newQuery[0] = upperLetters[m]
                        if ''.join(newQuery) in self._words and not (''.join(newQuery) in suggestions):
                            suggestions.append(''.join(newQuery))

            # Changing every character to a lowercase character
            for k in range(len(query)):
                newQuery = list(query)
                for l in range(len(lowerLetters)):
                    newQuery = list(query)
                    newQuery[k] = lowerLetters[l]
                    if ''.join(newQuery) in self._words and not (''.join(newQuery) in suggestions):
                        suggestions.append(''.join(newQuery))
            
            # Changing the first letter to uppercase
            newQuery = list(query)
            newQuery[0] = newQuery[0].upper()
            if ''.join(newQuery) in self._words and not (''.join(newQuery) in suggestions):
                suggestions.append(''.join(newQuery))
        
        return sorted(suggestions)