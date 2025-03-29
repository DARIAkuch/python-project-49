import random

from brain_games.engine.game_engine import run_game

def is_even(digit):
    return digit % 2

def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "no" if is_even(number) else "yes"
    return question, correct_answer

def main():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_question_and_answer, game_rule, "Even Game")

if __name__ == '__main__':
    main()