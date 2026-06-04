# ============================================================
#  General Knowledge Quiz — Project 4
# ============================================================

import time
import random

# ── helpers ─────────────────────────────────────────────────

def divider(char="─", width=52):
    print(char * width)

def slow_print(text, delay=0.018):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def get_answer():
    raw = input("     Your answer: ")
    return raw.strip().lower()

def ask(number, question, correct_answers, hint=None):
    slow_print(f"\n  Q{number}  {question}", delay=0.014)
    print("  >>")
    user = get_answer()

    if user in correct_answers:
        print("  [ CORRECT ]  +1 point\n")
        return 1
    else:
        msg = f"  [ WRONG ]  Correct answer: {correct_answers[0].capitalize()}"
        if hint:
            msg += f"\n  Hint: {hint}"
        print(msg + "\n")
        return 0

def grade(score, total):
    ratio = score / total
    if   ratio == 1.0:  return "Perfect score — outstanding work!"
    elif ratio >= 0.67: return "Great job — almost perfect."
    elif ratio >= 0.34: return "Good effort — keep practising."
    else:               return "Don't give up — review and retry!"

# ── question bank ─────────────────────────────────────────────
#  Format: ("question text", ["answer1", "answer2", ...], "hint")

QUESTIONS = [
    (
        "What is the capital city of France?",
        ["paris"],
        "It is famous for the Eiffel Tower."
    ),
    (
        "Which planet is closest to the Sun?",
        ["mercury"],
        "It is the smallest planet in our solar system."
    ),
    (
        "How many sides does a hexagon have?",
        ["6", "six"],
        "Think of a honeycomb cell."
    ),
    (
        "What is the chemical symbol for water?",
        ["h2o"],
        "Two hydrogen atoms and one oxygen atom."
    ),
    (
        "Which country is the largest in the world by area?",
        ["russia"],
        "It spans across Eastern Europe and Northern Asia."
    ),
    (
        "How many continents are there on Earth?",
        ["7", "seven"],
        "Africa, Antarctica, Asia, Australia, Europe, North America, South America."
    ),
    (
        "What is the fastest animal on land?",
        ["cheetah"],
        "It can reach speeds of up to 120 km/h."
    ),
    (
        "Which ocean is the largest in the world?",
        ["pacific", "pacific ocean"],
        "It covers more than 30% of the Earth's surface."
    ),
    (
        "In which year did World War II end?",
        ["1945"],
        "It ended after the atomic bombings of Hiroshima and Nagasaki."
    ),
    (
        "What is the hardest natural substance on Earth?",
        ["diamond"],
        "It scores a 10 on the Mohs hardness scale."
    ),
    (
        "How many bones are in the adult human body?",
        ["206"],
        "Babies are born with around 270 bones that fuse over time."
    ),
    (
        "What gas do plants absorb from the atmosphere?",
        ["carbon dioxide", "co2"],
        "Plants use it during photosynthesis."
    ),
    (
        "What is the capital city of Japan?",
        ["tokyo"],
        "It is the most populous metropolitan area in the world."
    ),
    (
        "Which element has the chemical symbol O?",
        ["oxygen"],
        "We breathe it to survive."
    ),
    (
        "How many players are on a football team on the field?",
        ["11", "eleven"],
        "Each team has the same number."
    ),
    (
        "What is the longest river in the world?",
        ["nile", "nile river"],
        "It flows through northeastern Africa."
    ),
    (
        "Which planet is known as the Red Planet?",
        ["mars"],
        "It has a reddish appearance due to iron oxide on its surface."
    ),
    (
        "What is the tallest mountain in the world?",
        ["mount everest", "everest"],
        "It is located in the Himalayas between Nepal and Tibet."
    ),
    (
        "How many hours are in a day?",
        ["24", "twenty four", "twenty-four"],
        "The Earth takes this long to complete one full rotation."
    ),
    (
        "What is the capital city of Egypt?",
        ["cairo"],
        "It is the largest city in Africa and the Arab world."
    ),
    (
        "Which gas makes up most of the Earth's atmosphere?",
        ["nitrogen"],
        "It makes up about 78% of the air we breathe."
    ),
    (
        "What is 12 multiplied by 12?",
        ["144", "one hundred and forty four"],
        "It is a perfect square number."
    ),
    (
        "Which continent is Brazil located in?",
        ["south america"],
        "It is the largest country on that continent."
    ),
    (
        "What is the smallest planet in our solar system?",
        ["mercury"],
        "It is also the closest planet to the Sun."
    ),
    (
        "How many days are in a leap year?",
        ["366"],
        "A leap year occurs every four years."
    ),
    (
        "What language is spoken in Brazil?",
        ["portuguese"],
        "It is different from most other South American countries."
    ),
    (
        "What is the boiling point of water in Celsius?",
        ["100", "100 degrees", "100c"],
        "Water turns into steam at this temperature."
    ),
    (
        "Which planet has the most moons in our solar system?",
        ["saturn"],
        "It is also famous for its spectacular rings."
    ),
    (
        "What is the currency of the United Kingdom?",
        ["pound", "pound sterling", "gbp"],
        "Its symbol is £."
    ),
    (
        "How many sides does a triangle have?",
        ["3", "three"],
        "It is the simplest polygon."
    ),
]

# ── how many questions per round ─────────────────────────────

QUESTIONS_PER_ROUND = 3

# ── main quiz engine ─────────────────────────────────────────

def run_quiz():
    divider("═")
    slow_print("  GENERAL KNOWLEDGE QUIZ", delay=0.025)
    divider("═")

    pool  = random.sample(QUESTIONS, k=QUESTIONS_PER_ROUND)
    score = 0

    for i, (question, correct_answers, hint) in enumerate(pool, start=1):
        score += ask(i, question, correct_answers, hint)

    divider()
    slow_print(f"\n  Final score : {score} / {QUESTIONS_PER_ROUND}", delay=0.025)
    slow_print(f"  Result      : {grade(score, QUESTIONS_PER_ROUND)}\n", delay=0.02)
    divider()

# ── entry point ──────────────────────────────────────────────

if __name__ == "__main__":
    run_quiz()
    play_again = input("\n  Play again? (yes / no): ").strip().lower()
    while play_again in ["yes", "y"]:
        run_quiz()
        play_again = input("\n  Play again? (yes / no): ").strip().lower()
    print("\n  Thanks for playing. Keep learning!\n")
