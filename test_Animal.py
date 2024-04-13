import unittest
import Animal

class Tests(unittest.TestCase):
    def test_standart_input(self):
        # Arrange
        animal = Animal.AnimalBuilder(Animal.Human, "Bob", 18, Animal.SexMale, Animal.ColorBlack)
        # Act
        # Assert
        self.assertEqual(str(animal), "Bob is 18 years old male black human")
    
    def test_invalid_input(self):
        # Arrange
        # Act
        # Assert
        with self.assertRaises(TypeError):
            Animal.AnimalBuilder("Human", "Bob", 18, Animal.SexMale, Animal.ColorBlack)
    
    def test_more_args(self):
        # Arrange
        # Act
        # Assert
        with self.assertRaises(TypeError):
            Animal.AnimalBuilder(Animal.Human, "Bob", 18, Animal.SexMale, Animal.ColorBlack, "hello")

    def test_build(self):
        # Arrange
        test_animal = Animal.AnimalBuilder(Animal.Human, "Bob", 18, Animal.SexMale, Animal.ColorBlack)
        # Act
        # Assert
        with self.subTest("test build_head"):
            with self.assertRaises(NotImplementedError):
                test_animal.build_head()
                
        with self.subTest("test build_chest"):
            with self.assertRaises(NotImplementedError):
                test_animal.build_chest()
                
        with self.subTest("test build_arms"):
            with self.assertRaises(NotImplementedError):
                test_animal.build_arms()
                
        with self.subTest("test build_legs"):
            with self.assertRaises(NotImplementedError):
                test_animal.build_legs()
                
        with self.subTest("test build_special_features"):
            with self.assertRaises(NotImplementedError):
                test_animal.build_special_features()


if __name__ == '__main__':
    unittest.main()