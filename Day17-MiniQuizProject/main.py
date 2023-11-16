from question_model import Quesion
from data import question_data
from quiz_brain import Quiz_brain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Quesion(question_text,question_answer)
    question_bank.append((new_question))

quiz=Quiz_brain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You are done!")
print("Your final score is : " + str(quiz.score) + "!")

