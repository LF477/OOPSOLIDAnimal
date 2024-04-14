import unittest
import Animal


class Tests(unittest.TestCase):
    def test_standart_input(self):
        # Arrange
        app = Animal.App()
        # Act
        with self.subTest("Human"):
            human = app.make_human("Bob", 18, "male", "black")
            # Assert
            self.assertEqual(str(human), "Bob is 18 years old male black human with 1 head, 1 chest, 2 arms, 2 legs, 0 special feature")
        # Act
        with self.subTest("Dog"):
            dog = app.make_dog("Dob", 8, "f", "w")
            # Assert
            self.assertEqual(str(dog), "Dob is 8 years old female white dog with 1 head, 1 chest, 2 arms, 2 legs, 0 special feature")
        # Act
        with self.subTest("Alien"):
            alien = app.make_alien("Bod", 57, "", "")
            # Assert
            self.assertEqual(str(alien), "Bod is 57 years old no sex no color alien with 1 head, 1 chest, 2 arms, 2 legs, 0 special feature")

    def test_invalid_input(self):
        # Arrange
        app = Animal.App()
        # Act
        # Assert
        with self.assertRaisesRegex(TypeError, "12 must has wrong type"):
            app.make_human(12, 18, "male", "black")

    def test_more_args(self):
        # Arrange
        app = Animal.App()
        # Act
        # Assert
        with self.assertRaises(TypeError):
            app.make_human("Bob", 18, "male", "black", 1)

    def test_several_animals(self):
        # Arrange
        app = Animal.App()
        # Act
        app.make_human("Bob", 18, "male", "black")
        app.make_human("Dob", 241, "male", "right color")
        app.make_alien("Bod", 57, "", "")
        app.make_dog("Dob", 8, "f", "w")
        # Assert
        self.assertEqual(len(app.get_all_animals(need_to_print=False)), 4)

    def test_different_parts_quantity(self):
        # Arrange
        app = Animal.App()
        # Act
        with self.subTest("Single names"):
            bob = app.make_human("Bob", 18, "male", "black", head=2, chest=1, arm=4, leg=1, special_feature=1)
            # Assert
            self.assertEqual(bob, "Bob is 18 years old male black human with 2 heads, 1 chest, 4 arms, 1 leg, 1 special feature")
        # Act
        with self.subTest("Single quantities"):
            bob = app.make_human("Bob", 18, "male", "black", head=1, chest=1, arm=1, leg=1, special_feature=1)
            # Assert
            self.assertEqual(bob, "Bob is 18 years old male black human with 1 head, 1 chest, 1 arm, 1 leg, 1 special feature")
        # Act
        with self.subTest("Plural names"):
            bob = app.make_human("Bob", 18, "male", "black", heads=2, chests=1, arms=4, legs=1, special_features=1)
            # Assert
            self.assertEqual(bob, "Bob is 18 years old male black human with 2 heads, 1 chest, 4 arms, 1 leg, 1 special feature")
        # Act
        with self.subTest("Plural quantities"):
            bob = app.make_human("Bob", 18, "male", "black", heads=2, chests=2, arms=2, legs=2, special_features=2)
            # Assert
            self.assertEqual(bob, "Bob is 18 years old male black human with 2 heads, 2 chests, 2 arms, 2 legs, 2 special features")
        # Act
        with self.subTest("Test if Bobs are all differnt"):
            # Assert
            self.assertEqual(len(app.get_all_animals(need_to_print=False)), 4)


if __name__ == '__main__':
    unittest.main()
