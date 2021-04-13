# URLify: Write a method to replace all spaces in a string with '%20'. You may assume 
# that the string has sufficient space at the end to hold the additional characters, and that  you are given the 
# "true" length of the string.

def main():
    word = "Mr John Smith   "

    word = URLify(word)
    print(word)

# My version
def URLify(str):
    
    stack = []
    tempWord = ""

    str = str.split(" ")

    for word in str:
        if word != "":
            stack.append(word)
    
    for temp in stack:
        tempWord+= temp
        tempWord+= "%20"

    tempWord = tempWord[:-3]

    return tempWord

# Book version
def URLify_CtCI(str):
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            #Replace spaces
            string[new_index - 3: new_index]='%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1
        
    return string


main()


