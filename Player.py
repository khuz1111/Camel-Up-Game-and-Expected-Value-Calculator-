class Player:
    def __init__(self, name):
        self.coins = 0
        self.cards = []
        self.name = name
    
    def __str__(self) -> str:
        return self.name