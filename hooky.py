import os


def printHeader(message):
    os.system('clear')
    print('='*len(message))
    print(message)
    print('='*len(message))


def validateGuess(guess):
    if len(guess) != 5:
        print('Expected %d letters and got %d' % (5, len(guess)))
        return False

    for character in guess:
        if character < 'A' or character > 'Z':
            print('Invalid character in string!')
            return False

    return True


def inputNames():
    names = []
    nameNum = 1
    while nameNum <= 5:
        name = input('%d. ' % nameNum)
        if name:
            names.append(name)
            nameNum += 1
        else:
            break

    return names


def presentMenu(names):
    for i in range(len(names)):
        print('%d. %s' % ((i + 1), names[i]))

    while True:
        try:
            selection = int(input('>> '))
            if selection < 1 or selection > len(names):
                print('Please enter a valid number from 1 to %d' % (len(names)))
            else:
                return selection
        except:
            print('Please enter a valid number from 1 to %d' % (len(names)))


def getWord():
    while True:
        guess = input('Enter your 5-letter word: ').upper()

        if validateGuess(guess):
            return guess


def main():
    # Ask for all the players
    while True:
        printHeader('Enter names on separate lines (empty to finish)')
        names = inputNames()
        if len(names) < 3:
            print('This game only supports 3 to 5 players!')
            input()
        else:
            break

    lettersByPlayers = {
        3: 7,
        4: 5,
        5: 4,
    }
    numLetters = lettersByPlayers[len(names)]
    playerLetters = []

    # Get each player's letters
    for name in names:
        while True:
            printHeader('%s, enter your %d letters' % (name, numLetters))
            letters = input('>> ').upper()
            if len(letters) != numLetters:
                print('Expected %d letters and got %d!' %
                      (numLetters, len(letters)))
                input()
            else:
                playerLetters.append(letters)
                break

    names.append('(Quit)')

    # Ask for words
    while True:
        printHeader('Who do you want to ask a question to?')
        selectedIndex = presentMenu(names)

        if selectedIndex == len(names):
            print('Thank you for playing!')
            break

        letters = playerLetters[selectedIndex - 1]

        guessedWord = getWord()

        count = 0
        for letter in guessedWord:
            if letter in letters:
                count += 1

        print('%s has %d of the letters in %s' %
              (names[selectedIndex-1], count, guessedWord))
        input()


main()