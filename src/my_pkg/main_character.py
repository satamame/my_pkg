from .character import Character


class MainCharacter(Character):
    def __init__(self, name='ヒロ', age=14):
        self.name = name
        super().__init__(age)
