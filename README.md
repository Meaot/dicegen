**DiceGen** is a simple Python script that generates passphrases based on the
[Diceware method](http://world.std.com/~reinhold/diceware.html).

### Randomness
The script calls the OS's `urandom` device to generate cryptographically
random bytes which are converted to integers and divided modulo 6 to create
the keys indicating words in the [Diceware wordlist](http://world.std.com/~reinhold/diceware.wordlist.asc).

### Usage
DiceGen takes one optional command line parameter - the length of the specified
passphrase (which must be between 5 and 10 words).

`python dicegen.py 7`

If not provided, the user is prompted to enter the desired length of the
passphrase.
