import os
import sys

WORDS = "diceware_wordlist.txt"

def exists_arg():
    """Checks if argv input was given."""
    return len(sys.argv) != 1


def test_arg(arg):
    """Checks if input is of the required form and returns
    various failure cases.
    """
    try:
        arg = int(arg)
    except ValueError:
        return 'Please enter an integer.'
    if arg < 5:
        return 'Length must be >= 5.'
    elif arg > 10:
        return 'Length must be <= 10'
    else:
        return 0, arg

def load_dict():
    """Returns a dictionary of the number to word mappings
    in the Diceware words file.
    """
    word_dict = {}
    with open(WORDS) as in_file:
        for line in in_file:
        	tmp = line.split()
        	key = tmp[0]
        	value = tmp[1]
        	word_dict[key] = value
    return word_dict

def generate_key():
    """Takes 6 bytes one at a time from the OS random device,
    converts them to integers, adds them together, and takes 
    the modulo 6 value as a piece of a 5 digit key.

    Returns a key for a value in the Diceware dictionary.
    """
    key = ''
    for _ in range(5):
        digit = 0
        for _ in range(6):
            digit += ord(os.urandom(1))
        key += str(digit%6 + 1)
    return key

def generate_passphrase(length):
    """Returns a randomly chosen passphrase based on desired length."""
    word_dict = load_dict()
    passphrase = ''
    for _ in range(length):
        key = generate_key()
        passphrase += word_dict[key] + ' '
    return passphrase

def main():
    flag = True
    while True:
        if flag and exists_arg():
            arg = sys.argv[1]
            flag = False
        else:
            arg = raw_input('Length of desired passphrase: ')
        check = test_arg(arg)
        if check[0] == 0:
            print generate_passphrase(check[1])
            return
        else:
            print check

if __name__ == '__main__':
    main()
