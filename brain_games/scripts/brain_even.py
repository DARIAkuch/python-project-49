import random

from brain_games.cli import welcome_user

import prompt

def is_even(digit):
    return digit % 2


def brain_even():
    name = welcome_user()
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(rule)
    counter = 0
    while counter < 3:
        digit = random.randint(1, 100)
        right_answer = is_even(digit)
        print(f"Question: {digit}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == 'yes':
            user_answer = False
        else:
            user_answer = True
        if right_answer == user_answer:
            print('Correct!')
            counter = counter + 1
        elif right_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'. "
                  f"Let's try again, {name}")
            return


if __name__ == '__main__':
    brain_even()