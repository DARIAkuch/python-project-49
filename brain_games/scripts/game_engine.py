from brain_games.scripts.utils import (
    welcome_user, ask_question, compare_answer, ROUND_LIMIT
)

def run_game(logic, rule, name):
    name = welcome_user()
    print(rule)
    round_counter = 0
    while round_counter < ROUND_LIMIT:
        question, correct_answer = logic()
        answer = ask_question(f'Question: {question}')
        success = compare_answer(answer, correct_answer)
        if success:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")