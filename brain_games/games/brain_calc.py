import random

from brain_games.scripts.game_engine import run_game

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

def main():
    game_rule = 'What is the result of the expression?'
    run_game(generate_question, game_rule, "Calculator Game")

if __name__ == '__main__':
    main()