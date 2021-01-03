import unittest

from my_pkg.character import Character
from my_pkg.main_character import MainCharacter


class TestInitChar(unittest.TestCase):
    '''各クラスのインスタンス初期化のテスト
    '''
    def test_init_character(self):
        character = Character()
        self.assertEqual(character.age, 17)
        character = Character(14)
        self.assertEqual(character.age, 14)

    def test_init_main_character(self):
        main_character = MainCharacter()
        self.assertEqual(main_character.age, 14)
        self.assertEqual(main_character.name, 'ヒロ')
