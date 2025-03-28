from random import randint

from brain_games.cli import welcome_user

import prompt

def generate_progression(start, step, length):
    return[start + i * step for i in range(length)]

def make_question_answer():
    length = randint(5, 10)
    step = randint(1, 10)
    start = randint(1, 10)
    progression = generate_progression(start, step, length)
    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    progression_string = " ".join(map(str, progression))
    question = progression_string
    return question, correct_answer

def brain_progression():
    name = welcome_user()
    rule = 'What number is missing in the progression?'
    print(rule)
    counter = 0
    while counter < 3:
        question, correct_answer = make_question_answer()
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
    brain_progression()

if __name__ == '__main__':
    main()