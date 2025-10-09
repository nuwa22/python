userName = input("What’s your name? ").capitalize()
print(f"Hello, {userName}! Let's start the quiz.\n")
numberOfQuestions = int(input("How many questions you choose to answer? "))

questions = {"What is the capital of France?": ["Parise", "London", "Berlin", "Parise"],
             "Which planet is known as the Red Planet?": ["Earth", "Venus", "Mars", "Mars"],
             "What color do you get when you mix red and blue?": ["Purple", "Green", "Orange", "Purple"],
             "How many days are there in a leap year?": ["365", "366", "364", "366"],
             "Which animal is known as the King of the Jungle?": ["Elephant", "Lion", "Tiger", "Lion"]}

score = 0
correctAnswers = []

for i in range(numberOfQuestions):
    question = list(questions.keys())[i]
    print(f"Q{i+1}: {question}")
    for j in range(3):
        print(f"{j+1}. {questions[question][j]}")
    answer = int(input("Your answer (1-3): "))
    if answer < 1 or answer > 3:
        print("Invalid choice. Please select a number between 1 and 3.\n")
    elif questions[question][answer - 1] == questions[question][3]:
        print("Correct!\n")
        score += 1
        correctAnswers.append(question)
    else:
        print(f"Wrong! The correct answer is {questions[question][3]}\n")

percentageScore = (score / numberOfQuestions) * 100

if percentageScore >= 80:
    performance = "Excellent"
elif 50 <= percentageScore < 80:
    performance = "Good"
else:
    performance = "Needs Improvement"
print(f"Quiz Over! You scored {score} out of {numberOfQuestions}. ({percentageScore:.2f}%) - {performance}")

