import re

class speech_text: 
    def speech_to_text(self,text):
        """This function converts a paragraph of spoken english to written english and returns transformed text
         
           Input : input text containing spoken words 
           Output : transformed text 
        """
        text = self.text2int(text)
        text = re.sub(r'dollar[s]*', '$', text)
        text = re.sub(r"(\d+)\s\$", r"$\1", text)
        text = re.sub(r"([A-Z])+\s([A-Z])+",r"\1\2", text)
        text = re.sub(r"[Tt]ripple\s(\w)+", r"\1\1\1", text )
        text = re.sub(r"[Dd]ouble\s(\w)+", r"\1\1", text )
        return text 
    
    
    # reference used : https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
    def text2int(self,textnum, numwords={}):
        """This function takes in a literal representation of numbers and returns numeric representation

           Input  : numbers in words example - two hundred thirty two 
           output : numeric representation of input example - 232 
        """
        
        if not numwords:
            units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
            ]

            tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            scales = ["hundred", "thousand", "million", "billion", "trillion"]

            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):  numwords[word] = (1, idx)
            for idx, word in enumerate(tens):   numwords[word] = (1, idx * 10)
            for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

        ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
        ordinal_endings = [('ieth', 'y'), ('th', '')]

        textnum = textnum.replace('-', ' ')

        current = result = 0
        curstring = ""
        onnumber = False
        for word in textnum.split():
            if word in ordinal_words:
                scale, increment = (1, ordinal_words[word])
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True
            else:
                for ending, replacement in ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in numwords:
                    if onnumber:
                        curstring += repr(result + current) + " "
                    curstring += word + " "
                    result = current = 0
                    onnumber = False
                else:
                    scale, increment = numwords[word]

                    current = current * scale + increment
                    if scale > 100:
                        result += current
                        current = 0
                    onnumber = True

        if onnumber:
            curstring += repr(result + current)

        return curstring