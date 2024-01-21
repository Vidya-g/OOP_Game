class Question():
    ''' Creating Question class for quiz '''    
    def __init__(self, question_text, options, correct_answer):
        self.question_text=question_text
        self.options= options
        self.correct_answer= correct_answer     

    def get_text(self):
        ''' return: questions for the game'''
        return self.question_text
    def get_options(self):
        ''' return: options for the game'''
        return self.options
    def get_answers(self,input_answer):
        ''' return: answer for the question'''
        return input_answer == self.correct_answer