import random

def get_number():  # funkcja pobiera liczbę, którą wskazał użytkownik
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")
    return result

def get_computer_number():
    """Main function with our game."""
    computer_number = random.randint(1, 10)
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
