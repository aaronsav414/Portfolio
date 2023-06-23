from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

print("You completed the quiz!")
print(f"Your score is {quiz.user_correct} out of {len(question_bank)} questions.")
