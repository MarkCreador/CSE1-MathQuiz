import random
import unittest

class MathQuiz:
    def __init__(self, num_questions=5):
        self.num_questions = num_questions
        self.score = 0
    
    def generate_question(self):
        """Generates a random math question with two operands and an operator."""
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        if operator == '/':
            num1 = num1 * num2
        
        question = f"{num1} {operator} {num2}"
        correct_answer = eval(question)
        
        return question, correct_answer
    
    def start_quiz(self):
        """Starts the quiz by asking questions and checking answers."""
        for i in range(self.num_questions):
            question, correct_answer = self.generate_question()
            user_answer = float(input(f"Question {i + 1}: What is {question}? "))
            
            if abs(user_answer - correct_answer) < 0.001:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        
        print(f"\nYour final score is {self.score} out of {self.num_questions}.")

class TestMathQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = MathQuiz(num_questions=1)

    def test_generate_question(self):
        """Test the question generation and correctness of the answer."""
        question, correct_answer = self.quiz.generate_question()
        self.assertIsInstance(question, str)
        self.assertIsInstance(correct_answer, (int, float))

        self.assertEqual(eval(question), correct_answer)

    def test_scoring(self):
        """Test if scoring system works correctly."""
        self.quiz.score = 0
        question, correct_answer = self.quiz.generate_question()

        if isinstance(correct_answer, float):
            user_answer = correct_answer
        else:
            user_answer = float(correct_answer)

        if abs(user_answer - correct_answer) < 0.001:
            self.quiz.score += 1

        self.assertEqual(self.quiz.score, 1)

if __name__ == "__main__":
    choice = input("Do you want to (P)lay the quiz or (T)est the program? ").lower()

    if choice == 'p':
        quiz = MathQuiz()
        quiz.start_quiz()
    elif choice == 't':
        unittest.main()