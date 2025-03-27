import random

from brain_games.cli import welcome_user

import prompt

def generate_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = a + b
    elif operator == '-':
        correct_answer = a - b
    else:
        correct_answer = a * b

    question = f"{a} {operator} {b}"
    return question, correct_answer

def brain_calc():
    name = welcome_user()
    rule = 'What is the result of the expression?'
    print(rule)
    counter = 0
    while counter < 3:
        question, correct_answer = generate_question()
        correct_answer = str(correct_answer)
        print(f'Question: {question}')
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
    brain_calc()
    
if __name__ == '__main__':
    main()