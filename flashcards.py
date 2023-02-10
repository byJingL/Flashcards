# Write your code here
import random
import io
import argparse
import re


def add():
    front = input(f'The card:\n')
    print(f'The card:\n{front}\n', file=output)

    while front in cards_dict:
        front = input(f'The card "{front}" already exists. Try again:\n')
        print(f'The card "{front}" already exists. Try again:\n{front}\n', file=output)

    back = input(f"The definition of the card:\n")
    print(f'The definition of the card:\n{back}\n', file=output)

    values = [value['definition'] for value in cards_dict.values()]
    while back in values:
        back = input(f'The definition "{back}" already exists. Try again:\n')
        print(f'The definition "{back}" already exists. Try again:\n{back}\n', file=output)

    cards_dict[front] = {
        'definition': back,
        'mistake': 0
    }

    print(f'The pair ("{front}":"{back}") has been added.')
    print(f'The pair ("{front}":"{back}") has been added.\n', file=output)


def remove():
    front = input(f'Which card?\n')
    print(f'Which card?\n{front}\n', file=output)

    if front in cards_dict:
        cards_dict.pop(front)
        print('The card has been removed.')
        print('The card has been removed.\n', file=output)
    else:
        print(f'Can\'t remove "{front}": there is no such card.')
        print(f'Can\'t remove "{front}": there is no such card.\n', file=output)


def ask(count):
    card_list = list(cards_dict.items())
    while count > 0:
        random_card = random.choice(card_list)
        term, value = random_card
        definition = value['definition']
        user_input = input(f'Print the definition of "{term}":\n')
        print(f'Print the definition of "{term}":\n{user_input}\n', file=output)

        if user_input == definition:
            print('Correct!')
            print('Correct!\n', file=output)
        else:
            cards_dict[term]['mistake'] += 1
            message = handle_wrong_answer(user_input, definition)
            print(message)
            print(message, end='\n', file=output)
        count -= 1


def _import(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
            pattern = r"(\w+): {'definition': '(\w+)', 'mistake': (\d+)}"
            for line in data:
                front = re.match(pattern, line).group(1)
                back = re.match(pattern, line).group(2)
                count = re.match(pattern, line).group(3)
                cards_dict[front] = {
                    "definition": back,
                    "mistake": int(count),
                }
        print(f'{len(data)} cards have been loaded.')
        print(f'{len(data)} cards have been loaded.\n', file=output)
    except FileNotFoundError:
        print('File not found.')
        print('File not found.\n', file=output)


def export(file_name):
    with open(file_name, 'a') as file:
        for (term, definition) in cards_dict.items():
            file.write(f'{term}: {definition}\n')
    print(f'{len(cards_dict)} cards have been saved.')
    print(f'{len(cards_dict)} cards have been saved.\n', file=output)


def log(file_name):
    with open(file_name, 'w') as file:
        contents = output.getvalue()
        print(contents, file=file)

    print("The log has been saved.")
    print("The log has been saved.\n", file=output)


def hardest_card():
    highest = 0
    hard_cards = []
    for term, value in cards_dict.items():
        num = value['mistake']
        if num == 0:
            continue
        elif num < highest:
            continue
        elif num > highest:
            hard_cards = [term]
            highest = num
        elif num == highest:
            hard_cards.append(term)

    if len(hard_cards) == 0:
        print('There are no cards with errors.')
        print('There are no cards with errors.\n', file=output)
    elif len(hard_cards) == 1:
        print(f'The hardest card is "{hard_cards[0]}". You have {highest} errors answering it.')
        print(f'The hardest card is "{hard_cards[0]}". You have {highest} errors answering it.\n', file=output)
    else:
        s = '", "'.join(hard_cards)
        print(f'The hardest cards are "{s}". You have {highest} errors answering them.')
        print(f'The hardest cards are "{s}". You have {highest} errors answering them.\n', file=output)


def rest_stats():
    for value in cards_dict.values():
        value['mistake'] = 0
    print('Card statistics have been reset.')
    print('Card statistics have been reset.\n', file=output)


def handle_wrong_answer(answer, correct_answer):
    for term, value in cards_dict.items():
        if answer == value['definition']:
            return f'Wrong. The right answer is "{correct_answer}", but your definition is correct for "{term}".'
    return f'Wrong. The right answer is "{correct_answer}".'


cards_dict = {}
output = io.StringIO()


def main():
    parser = argparse.ArgumentParser()
    # optional arguments for parser
    parser.add_argument('--import_from', help='Input the name of file you want to import from')
    parser.add_argument('--export_to', help='Input the name of file you want to export to')
    args = parser.parse_args()

    if args.import_from:
        _import(args.import_from)

    while True:
        intro_message = 'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n'
        action = input(intro_message).strip().lower()
        print(f'{intro_message}{action}\n', file=output)

        if action == 'add':
            add()

        if action == 'remove':
            remove()

        if action == 'import':
            file_name = input('File name:\n')
            print(f'File name:\n{file_name}\n', file=output)
            _import(file_name)

        if action == 'export':
            file_name = input('File name:\n')
            print(f'File name:\n{file_name}\n', file=output)
            export(file_name)

        if action == 'ask':
            count = int(input('How many times to ask?\n'))
            print(f'How many times to ask?\n{count}\n', file=output)
            ask(count)

        if action == 'log':
            file_name = input('File name:\n')
            print(f'File name:\n{file_name}\n', file=output)
            log(file_name)

        if action == 'hardest card':
            hardest_card()

        if action == 'reset stats':
            rest_stats()

        if action == 'exit':
            if args.export_to:
                export(args.export_to)
                quit()
            else:
                print('Bye bye!')
                quit()


if __name__ == "__main__":
    main()
