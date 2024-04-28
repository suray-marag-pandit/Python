def quiz_game():
    questions = {
        "What is the output of 3 + 2 * 2?": "a",
        "In Python, how do you insert COMMENTS?": "a",
        "Which function in Python can be used to check if an object is an integer or not?": "c",
        "How do you create a list in Python?": "a",
        "What keyword is used to create a function in Python?": "b"
    }
    options = [
        ["a) 7", "b) 10", "c) 5", "d) None of the above"],
        ["a) # This is a comment", "b) <!-- This is a comment -->", "c) /* This is a comment */",
         "d) // This is a comment"],
        ["a) int()", "b) isdigit()", "c) isinstance()", "d) isint()"],
        ["a) []", "b) ()", "c) {}", "d) ||"],
        ["a) function", "b) def", "c) func", "d) create"]
    ]

    score = 0
    for i, (question, correct_answer) in enumerate(questions.items()):
        print(f"Q{i + 1}: {question}")
        for option in options[i]:
            print(option)
        user_answer = input("Enter your answer (a, b, c, or d): ").lower()
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print()  # Print a newline for better spacing between questions

    print(f"Game Over! Your score was: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()
