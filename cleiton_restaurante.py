database = [{'cod': 1, 'item': 'Lanchinho Kids', 'value': 6.00},
            {'cod': 2, 'item': 'Bacon Lanche', 'value': 11.50},
            {'cod': 3, 'item': 'Bacon Egg Lanche', 'value': 16.00},
            {'cod': 4, 'item': 'Chicken Lanche', 'value': 15.00},
            {'cod': 5, 'item': 'Chicken Bacon Lanche', 'value': 17.50}]


def calc_value(cod: int, qtd: int) -> float:
    result = 0.0
    for item in database:
        if item['cod'] == cod:
            value = item['value']
            result = float(value * qtd)
    return result


def main():
    value_input = input()
    cod, qtd = value_input.split(' ')
    cod = int(cod)
    qtd = int(qtd)
    print(f'R$ {calc_value(cod, qtd):.2f}')


if __name__ == '__main__':
    main()
