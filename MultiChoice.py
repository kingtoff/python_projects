from Question import question

question_prompts = ["What are you doing? \n (a) playing\n (b) sleeping\n (c) working\n\n",
 "which of this is an aws service?\n (a) driving \n (b) EC2 \n (c) azure \n\n", 
"who is the current twitter CEO?\n (a) jeff bezoz\n (b) fortune ogunwusi\n (c) elon musk\n\n"

]

questions = [
    question(question_prompts[0], "c"),
    question(question_prompts[1], "b"),
    question(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " of " + str(len(questions)) + " questions " + " correct!")            

run_test(questions)