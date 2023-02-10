# Flaskcards
This program can be used to remember any sort of data. It can record users'  learning progress by importing and exporting file.

Functions supported:
- `add`: add a card
- `remove`: remove a card
- `import`: load cards from file
- `export`: save cards to file
- `ask`: ask for definitions of some random cards
- `log`: save the application log to the given file
- `hardest card`: print the term or terms that the user makes most mistakes with
- `reset stats`: erase the mistake count for all cards
- `exit`: exit the program
  
## Main Skill
[io module](https://docs.python.org/3/library/io.html#text-i-o), [logging module](https://docs.python.org/3/library/logging.html), re module

## How to use
- Download [flashcards.py](/flashcards.py)
- Run [flashcards.py](/flashcards.py) with two optional arguments:
    - These two arguments can be used at the same time.
    - If you want to load cards:
    ```
    python3 flashcards.py --import_from=YourCardFile.txt
    ```
    - If you want to save the cards:
    ```
    python3 flashcards.py --export_from=YourCardFile.txt
    ```
- The file you want to load should better in follow format:
    ```
    Canada: {'definition': 'Ottawa', 'mistake': 34}
    Japan: {'definition': 'Tokyo', 'mistake': 39}
    Poland: {'definition': 'Warsaw', 'mistake': 27}
    ```
 
## Example
```
python3 flashcards.py --import_from=test.txt --export_from=test.txt
```
```
3 cards have been loaded.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The card:
> Texas
The definition of the card:
> Austin
The pair ("Texas":"Austin") has been added.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The card:
> Florida
The definition of the card:
> Tallahassee
The pair ("Florida":"Tallahassee") has been added.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> ask
How many times to ask?
> 1
Print the definition of "Florida":
> Austin
Wrong. The right answer is "Tallahassee", but your definition is correct for "Texas".
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> exit
3 cards have been saved.
Bye bye!
```

## Disclaimer
The original learning materials and project ideas are from [JetBrains Academy](https://www.jetbrains.com/academy/). All codes were written by myself.
