def points_for_char(c):
    # Point Values
    scoring = {
        'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    return scoring.get(c, 0)


if __name__ == '__main__':
    while True:
        confirmation = ['y', 'Y', 'Yes', 'yES', 'YES', 'yes', 'YE', 'Ye', 'ye']
        word = ''
        while not word or word == ' ':
            word = input('\nWhat Scrabble word would you like me to score?\n')

        splitWord = list(word.upper())
        score = 0
        multiplier = 1

        doubled = input('\nWill your word be on a double word space?\n')
        if confirmation.__contains__(doubled):
            double_spaces = input('\nHow many of these spaces are hit?\n')
            multiplier *= 2 * int(double_spaces)

        tripled = input('\nWill your word be on a triple word space?\n')
        if confirmation.__contains__(tripled):
            triple_spaces = input('\nHow many of these spaces are hit?\n')
            multiplier *= 3 * int(triple_spaces)

        for char in splitWord:
            score += points_for_char(char)

        print(f'{word.upper()} is worth {score * multiplier} points.\n')

        response = input('Do you want to score another word?\n')
        if not confirmation.__contains__(response):
            break
