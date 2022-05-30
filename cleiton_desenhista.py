
value = 39
word = 'zappts'


def print_word(word, index):
    print(word[index], end='')


def print_square(value):
    print('aqui')
    for i in range(value):
        for j in range(value):
            if i == 0 or i == value - 1:
                print('-', end='')
                if j == value - 1:
                    print()

            elif j == 0 or j == value - 1:
                print('|', end='')
                if j == value - 1:
                    print()

            elif (i == 1 or i == value - 2) and (j > 0 and j < 7):
                    print_word(word, j - 1)
            else:
                print(' ', end='')


def main():
    print_square(value)


if __name__ == '__main__':
    main()