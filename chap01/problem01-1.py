# Is Unique: Implement an algorithm to determine if a string has all unique characters.
#            What if you cannot use additional data structures?

def main():
    testList = ["Hello, World!", "test", "makeshift"]

    for x in testList:
        if IsUnique01(x):
            print("Is Unquie")
        else:
            print("Is not Unqiue")

def IsUnique(strTest):
    arr = [0] * 256
    for letter in strTest:
        arr[ord(letter) - 0] = arr[ord(letter) - 0 ] + 1
    
    for x in arr:
        if x > 1:
            return False

    return True

def IsUnique01(strTest):

    # only 128 characters testing for.
    if len(strTest) > 128:
        return False

    charSet = [False for _ in range(128)]

    for char in strTest:
        val = ord(char)
        if charSet[val]:
            #Char in set already
            return False
        charSet[val] = True

    return True

main()