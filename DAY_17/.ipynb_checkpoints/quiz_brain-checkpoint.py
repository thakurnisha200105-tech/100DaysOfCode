# QuizBrain has two attribute :- question_number = 0 and questions_list , Methods : next_question()




# Create a class called QuizBrain. Write an __init__() method., Initialise the question_number to 0. Initialise the question_list to an input.

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    # Retrieve the item at the current question_number from the question_list.
    # Use the input() function to show the user the Question text and ask for the user's answer
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{sef.question_number}:{current_question.text} (True/false):")