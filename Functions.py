# functions
# - consists of function name, parameters.
# - starts "def" keyword.
# - Optimizes and make a block of code reuseable.

def averageOfThreeNumbers(num1, num2, num3):
    #codes...
    average = (num1 + num2 + num3) / 3
    print("Average: ", average)

#SHORTCUT FOR COPYING HIGHLIGHTED/SINGLE LINE: alt + shift + ArrowDown/ArrowUp
    
    averageOfThreeNumbers(89, 76, 81)
    averageOfThreeNumbers(89, 76, 81)
    averageOfThreeNumbers(89, 76, 81)

#Return function
    title = "Ang Alamat ni Loudie"
    title2 = ": Bagsakan Era"

    def stringToTitle(title):
        return title.title()
    
    def stringToUpperCase(message):
        return message.upper()
    
    def stringToLowerCase(message):
        return message.lower()
    
    def joinString(message, message2):
        return message.join(message2)
    
    def countLetters(message):
        return len(message)
        
    print(stringToTitle(title))    
    print(stringToUpperCase(title))    
    print(stringToLowerCase(title))   
    print(joinString(title, title2)) 
    print(countLetters(title))    