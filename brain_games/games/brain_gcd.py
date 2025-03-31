import random
from math import gcd

from brain_games.scripts.game_engine import run_game


def generate_question():
    right_num = random.randint(1, 100)
    left_num = random.randint(1, 100)
    correct_answer = gcd(left_num, right_num)
    question = f"{left_num} {right_num}"
    return question, correct_answer


def main():
    game_rule = 'Find the greatest common divisor of given numbers.'
    run_game(generate_question, game_rule, "Find Greatest Common Divisor")


if __name__ == '__main__':
    main()