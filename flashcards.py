# Write your code here
import random


def add_cards(cards_dict):
    term = input(f'The card:\n')
    while term in cards_dict:
        term = input(f'The card "{term}" already exists. Try again:\n')

    definition = input(f"The definition of the card:\n")
    values = [*cards_dict.values()]
    while definition in values:
        definition = input(f'The definition "{definition}" already exists. Try again:\n')

    cards_dict[term] = definition
    print(f'The pair ("{term}":"{definition}") has been added.')


def remove_cords(cards_dict):
    term = input(f'Which card?\n')
    if term in cards_dict:
        cards_dict.pop(term)
        print('The card has been removed.')
    else:
        print(f'Can\'t remove "{term}": there is no such card.')


def import_file(file_name, cards_dict):
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
            for line in data:
                cards_dict[line.split()[0]] = line.split()[-1]
        print(f'{len(data)} cards have been loaded.')
    except FileNotFoundError:
        print('File not found.')


def export_file(file_name, cards_dict):
    with open(file_name, 'a') as file:
        for (term, definition) in cards_dict.items():
            file.write(f'{term}: {definition}\n')
    print(f'{len(cards_dict)} cards have been saved.')


def ask_cards(count, cards_dict):
    cards = [*cards_dict.keys()]
    for _ in range(count):
        term = random.choice(cards)
        user_input = input(f'Print the definition of "{term}":\n')
        if user_input == cards_dict[term]:
            print('Correct!')
        else:
            message = handle_wrong_answer(term, user_input, cards_dict)
            print(message)


def handle_wrong_answer(term, answer, cards):
    for card in cards:
        if answer == cards[card]:
            return f'Wrong. The right answer is "{cards[term]}", but your definition is correct for "{card}".'
    return f'Wrong. The right answer is "{cards[term]}".'


def main():
    cards_dict = {}

    while True:
        action = input('Input the action (add, remove, import, export, ask, exit):\n')
        if action == 'add':
            add_cards(cards_dict)

        if action == 'remove':
            remove_cords(cards_dict)

        if action == 'import':
            file_name = input('File name:\n')
            import_file(file_name, cards_dict)

        if action == 'export':
            file_name = input('File name:\n')
            export_file(file_name, cards_dict)

        if action == 'ask':
            count = int(input('How many times to ask?\n'))
            ask_cards(count, cards_dict)

        if action == 'exit':
            print('Bye bye!')
            quit()


if __name__ == "__main__":
    main()
