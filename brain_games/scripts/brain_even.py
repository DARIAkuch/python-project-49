import random

from brain_games.cli import welcome_user

import prompt

from brain_games.engine.game_engine import run_game

def is_even(digit):
    return digit % 2

def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "no" if is_even(number) else "yes"
    return question, correct_answer


def brain_even():
    name = welcome_user()
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(rule)
    counter = 0
    while counter < 3:
        question, answer = generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
            counter = counter + 1
        elif answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'. "
                  f"Let's try again, {name}")
            return
    print(f'Congratulations, {name}')

def main():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_question_and_answer, game_rule, "Even Game")

if __name__ == '__main__':
    main()