class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number=0
        self.score = 0

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Question {self.question_number}: {current_question.text}(true/false): ")
        self.check_answer(user_answer,current_question.answer)
    @property
    def still_has_questions(self):
         return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("Correct!")
            self.score += 1

        else :
            print("Incorrect!")
            print(f"correct answer was: {answer}")
        print(f"your score was: {self.score}/{self.question_number}")