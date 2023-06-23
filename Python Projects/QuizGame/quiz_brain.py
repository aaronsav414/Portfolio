class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.user_correct = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} True/False: ").lower()
        self.check_answer(user_answer, current_question)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, current_question):
        if user_answer == current_question.correct_answer.lower():
            self.user_correct += 1
            print("Correct!")
        else:
            print("Wrong!")

        print(f"The correct answer is: {current_question.correct_answer}.")
        print(f"Your score is: {self.user_correct}/ {self.question_number}")
        print("\n")