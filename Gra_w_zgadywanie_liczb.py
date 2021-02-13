import random

def get_number():
    """ Funkcja pobiera liczbę, którą wskazał użytkownik.
        Pyta dopóki nie otrzyma poprawnej liczby.
        :rtype: int
        :return: pobrana liczba jako int
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")
    return result

def get_computer_number():
    """ Main function with our game.
        Główna funkcja losuje liczbę w zakresie 1 – 100
        oraz zwraca informację czy liczba jest za mała, za duża czy równa wylosowanej.
    """
    computer_number = random.randint(1, 100)
    guess_number = get_number()
    while guess_number != computer_number:
        if guess_number < computer_number:
            print("To small!")
        else:
            print("To big!")
        guess_number = get_number()
    print("You win!")

if __name__ == '__main__':
    get_computer_number()
