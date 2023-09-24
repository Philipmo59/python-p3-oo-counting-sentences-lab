#!/usr/bin/env python3

class MyString:
    def __init__(self, value ='') -> None:
        self._value = value 
    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def get_value(self):
        return self._value
    
    value = property(get_value,set_value)

    def is_sentence(self):
        return self._value.endswith(".") 
        #returns true or false (endswith)
    def is_question(self):
      return self._value.endswith("?") 
    def is_exclamation(self):
      return self._value.endswith("!") 
    
    def count_sentences(self):
        value = self.value 
        for punc in ["!","?"]:
            value = value.replace(punc, ".")
        sentences = [s for s in value.split(".") if s]  
        print(len(sentences))
        return len(sentences)
sentence = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
sentence.count_sentences()
sentence.is_question()


    
    