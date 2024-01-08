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
    while True:
        name = input()
        if name:
            names.append(name)
        else:
            break
    return names


def presentMenu(names):
    for i in range(len(names)):
        print('%d. %s' % ((i + 1), names[i]))

    print('>> ',)
    return int(input())


def getWord(numLetters):
    while True:
        print('Enter your 5-letter word: ',)
        guess = input().upper()

        if validateGuess(guess, numLetters):
            return guess


def main():
    # Ask for all the players
    printHeader('Enter names on separate lines (empty to finish)')
    names = inputNames()

    numLetters = 20 // len(names)
    playerLetters = []

    # Get each player's letters
    for name in names:
        while True:
            printHeader('%s, enter your %d letters' % (name, numLetters))
            letters = input().upper()
            if len(letters) != numLetters:
                print('Expected %d letters and got %d! Press enter to retry.' %
                      (numLetters, len(letters)))
                input()
            else:
                playerLetters.append(letters)
                break

    print(names)
    print(playerLetters)

    # Ask for words
    while True:
        printHeader('Who do you want to ask a question to?')
        selectedIndex = presentMenu(names)

        if selectedIndex < 1 or selectedIndex > len(names):
            print('Invalid player!')
            continue

        letters = playerLetters[selectedIndex - 1]

        guessedWord = getWord(numLetters)

        count = 0
        for letter in guessedWord:
            if letter in letters:
                count += 1

        print('%s has %d of the letters in %s' % (name, count, guessedWord))
        input()


main()
