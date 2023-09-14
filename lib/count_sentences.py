class MyString:
    def __init__(self, value = ""):
        self.value = value
    
    @property
    def value(self):
        return self._value
  
    @value.setter
    def value(self, value):
        if isinstance(value, str) == False:
            print("The value must be a string.")
        else:
            self._value = value
      
    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False
        
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False
          
    def count_sentences(self):
        value = self.value
        for punc in ["?", "!"]:
            value = value.replace(punc, ".")
        sentences = [s for s in value.split(".") if s]
        return len(sentences)
            
        