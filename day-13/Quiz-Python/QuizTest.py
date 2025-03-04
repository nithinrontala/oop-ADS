
from Solution import Question, Quiz

# main.py
def main():
    quiz = Quiz()
    
    # 1. Manually load quiz questions in main.
    data = (
        "Who is the current Chief Minister of Telangana?:Revanth Reddy,Chandra Babu Naidu,President’s Rule,Jagan:1:3:-1\n"
        "What is the capital of France?:Paris,London,Rome,Berlin:1:2:0\n"
        "Which planet is known as the Red Planet?:Earth,Mars,Jupiter,Venus:2:4:-2"
    )
    
    # 2. Test parseQuestions method.
    quiz.parseQuestions(data)
    if len(quiz.questions) == 3:
        print("parseQuestions Test: PASS")
    else:
        print(f"parseQuestions Test: FAIL - Expected 3 questions, got {len(quiz.questions)}")
    
    # Additional tests for individual question parsing.
    individual_tests_passed = True
    if quiz.questions[0].question_text != "Who is the current Chief Minister of Telangana?":
        individual_tests_passed = False
        print("Test Failed: Incorrect question text for question 1.")
    if quiz.questions[1].max_marks != 2:
        individual_tests_passed = False
        print("Test Failed: Incorrect max marks for question 2.")
    if quiz.questions[2].penalty != -2:
        individual_tests_passed = False
        print("Test Failed: Incorrect penalty for question 3.")
    if individual_tests_passed:
        print("Individual Question Parsing Tests: PASS")
    
    # 3. Test startQuiz method.
    # Simulate answers: Q1 correct (1), Q2 wrong (2), Q3 correct (2).
    test_answers = [1, 2, 2]
    quiz.startQuiz(test_answers)
    
    quiz_test_passed = True
    # For Q1, expected score is max marks = 3.
    if quiz.questions[0].score != quiz.questions[0].max_marks:
        quiz_test_passed = False
        print("startQuiz Test Failed: Question 1 score incorrect.")
    # For Q2, expected score is penalty = 0.
    if quiz.questions[1].score != quiz.questions[1].penalty:
        quiz_test_passed = False
        print("startQuiz Test Failed: Question 2 score incorrect.")
    # For Q3, expected score is max marks = 4.
    if quiz.questions[2].score != quiz.questions[2].max_marks:
        quiz_test_passed = False
        print("startQuiz Test Failed: Question 3 score incorrect.")
    if quiz_test_passed:
        print("startQuiz Test: PASS")
    
    # 4. Test total score calculation.
    expected_total = quiz.questions[0].max_marks + quiz.questions[1].penalty + quiz.questions[2].max_marks
    if quiz.total_score == expected_total:
        print("Total Score Calculation Test: PASS")
    else:
        print(f"Total Score Calculation Test: FAIL - Expected {expected_total}, got {quiz.total_score}")
    
    # 5. Finally, display the score report.
    print("\n--- Score Report ---")
    quiz.scoreReport()

if __name__ == '__main__':
    main()
