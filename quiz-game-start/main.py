from question_model import quetion
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data :
    Question_text = question["text"]
    Question_answer = question["answer"]
    new_question = quetion(Question_text, Question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_questions:
    quiz.next_question()
print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")