quiz = {
    "question1": {
        "question": "whats up \n",
        "answer": "paris"
    },
    "question2": {
        "question": "whats up \n",
        "answer": "gc"
    },
    "question3": {
        "question": "whats up \n",
        "answer": "tajj"
    },
    "question4": {
        "question": "whats up \n",
        "answer": "SA"
    },
}
score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("answer")

    if answer.lower() ==value['answer'].lower():
        print("Correct")
        score+=1
        print("ur score is "+ str(score))
        print("")
        print("")
    else:
        print("wrong answer")
        print("the answer is : "+ value['answer'])
        print("")
        print("")

print("u got "+ str(score) + " 0ut 0f 4 questions correctly")
print("your percentage is "+ str(score/4 * 100) + "%")      