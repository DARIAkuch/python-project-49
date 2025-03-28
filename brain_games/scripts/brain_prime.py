from random import randint

from brain_games.cli import welcome_user

import prompt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_question_answer():
    number = randint(0, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer

def brain_prime():
    name = welcome_user()
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(rule)
    counter = 0
    while counter < 3:
        question, correct_answer = generate_question_answer()
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
    brain_prime()

if __name__ == '__main__':
    main()