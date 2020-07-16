import random
import string

# Generate a string of random letters (upper + lower cases), numbers, and special characters
def GeneratePassword(len):
    # Min length for most passwords is 8
    if len < 8:
        return

    pool = ''

    # Get the num of uppercase
    upperLen = len // 4
    uppers = GenUppercase(upperLen)

    # Get the num of lowercases
    lowerLen = len //4
    lowers = GenLowercase(lowerLen)

    # Get the num of numbers
    numLen = len // 4
    nums = GenNum(numLen)

    # Get the num of special char
    numChar = len - upperLen - lowerLen - numLen
    specials = GenSpecialChar(numChar)

    # Connect all substrings
    pool += uppers + lowers + nums + specials

    # Shuffle the string
    l = list(pool)
    random.shuffle(l)
    pool = ''.join(l)

    return pool

# Generate random uppercase letters
def GenUppercase(len):
    pool = string.ascii_uppercase
    selected = ''.join(random.choice(pool) for i in range(len))

    return selected

# Generate random lowercase letters
def GenLowercase(len):
    pool = string.ascii_lowercase
    selected = ''.join(random.choice(pool) for i in range(len))

    return selected

# Generate random numbers
def GenNum(len):
    pool = string.digits
    selected = ''.join(random.choice(pool) for i in range(len))

    return selected

# Generate random special chars
def GenSpecialChar(len):
    pool = string.punctuation
    selected = ''.join(random.choice(pool) for i in range(len))

    return selected
