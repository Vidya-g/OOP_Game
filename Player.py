class Player():
    ''' Creating Player class'''
    def __init__(self, name):
        self.name= name
        self.score= 0   
    def get_name(self):
        ''' return: name of the player'''
        return self.name    
    def get_score(self):
        ''' return: score of the player '''
        return self.score