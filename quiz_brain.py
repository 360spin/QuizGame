class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        new_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {new_question.text} True or False?\n")
        self.question_number += 1
        self.check_answer(answer, new_question.answer)

    def check_answer(self, user_choice, correct_answer):
        if user_choice == correct_answer:
            print("You were right!")
            self.score += 1
        else:
            print("You are wrong! ")

        print(f"Correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

