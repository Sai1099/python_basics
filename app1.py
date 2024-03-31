from Question import Question
# Your remaining code
question_prompts = [
    "What Color is Your buggatti\n (a) orange\n (b) red\n (c) green",
    "What Color is Your banana\n (a) dicky\n (b) purple\n (c) yellow",
    "What Color is Your laptop\n (a) chrome\n (b) silver\n (c) black",
    "What Color is Your bike\n (a) blue\n (b) red\n (c) Ash"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer.lower():
            score += 1
    print(str(score))

run_test(questions)
