class analysedText(object):
    
    # Remove the punctuation from <text> and make it lower case.
    # Assign the formatted text to a new attribute called "fmtText"
    def __init__ (self, text):
        punctuations = (".", "!", ",", "?")
        for r in punctuations:
            text = text.replace(r,"")
        
        self.fmtText = text.lower()
    
    def freqAll(self):    
        words = self.fmtText.split()
        wordset = set(words)
        
        dict = {}
        for word in wordset:
            dict[word] = words.count(word)

        return dict

    def freqOf(self, word):
        dict = self.freqAll()
        return dict[word]
    