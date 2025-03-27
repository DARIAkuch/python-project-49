import random

from brain_games.cli import welcome_user

from math import gcd

import prompt

def generate_question():
    right_num = random.randint(1, 100)
    left_num = random.randint(1, 100)
    correct_answer = gcd(left_num, right_num)
    question = f"{left_num} {right_num}"
    return question, correct_answer

def brain_gcd():
    name = welcome_user()
    rule = "Find the greatest common divisor of given numbers."
    print(rule)
    counter = 0
    while counter < 3:
        question, correct_answer = generate_question()
        correct_answer = str(correct_answer)
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            counter = counter + 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}")
            return
    print(f'Congratulations, {name}')

def main():
        brain_gcd()

if __name__ == '__main__':
        main()