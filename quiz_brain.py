# Asking the user questions
# Checking if the answer was correct
# checking if we are the end of the quiz
# from main_question_model import question_bank

class QuizBrain:
    def __init__(self,question_object_lst):
        self.question_number =0
        self.score  = 0
        self.question_object_lst = question_object_lst

    def still_has_questions(self):
        return self.question_number<len(self.question_object_lst)


    def next_question(self):
        current_question = self.question_object_lst[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer,current_question.answer)


    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That is wrong")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current is : {self.score}/{self.question_number}")
        print("\n")
