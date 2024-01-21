class Game():
    def __init__(self, player, question):
        self.player= player
        self.question=question

    # def add_player(self):
    #     return self.player  
    # def add_questions(self):
    #     return self.question     
    def initialize_game(self):
        '''Add players and questions here'''
        self.execute_round()
    def execute_round(self):
        '''Execute game here'''
        player =  self.player
        question = self.question
        print(f"\n{player.get_name()}'s turn:")
        print(question.get_text())
        print("Options:", question.get_options())

        user_answer = input("Your answer: ")
        if question.get_answers(user_answer):
               # player.update_score(1)
            print("Correct! 1 point added.")
        else:
            print("Incorrect!")

    def play_game(self):
        '''intializing game here'''
        self.initialize_game()
