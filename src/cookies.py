import random

class CookieBowl(object):
    def __init__(self,vanilla=None):
        self.vanilla_like = vanilla
    
    def draw(self):
        chance = random.uniform(0,1)
        return 'Vanilla' if self.vanilla_like > chance else 'Chocolate' 
