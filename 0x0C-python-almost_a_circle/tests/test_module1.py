#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestClass(unittest.TestCase):

    def setUp(self):
        self.rec = Rectangle(10, 11, 1, 2)
        self.rec2 = Rectangle(10, 11, 1, 2)

    def test_init(self):
        """test the ___init___ method"""
        self.assertEqual(self.rec.width, 10)
        self.assertEqual(self.rec.height, 11)
        self.assertEqual(self.rec.x, 1)
        self.assertEqual(self.rec.y, 2)

    def test_width_setter(self):
        """testing the width setter"""
        with self.assertRaises(TypeError):
            self.rec.width = "2"
        with self.assertRaises(ValueError):
            self.rec.width = -1

    def test_height_setter(self):
        """
        testing the height setter
        """
        with self.assertRaises(TypeError):
            self.rec.height = "2"
        with self.assertRaises(ValueError):
            self.rec.height = -1

    def test_x_setter(self):
        """
        testing the x setter
        """
        with self.assertRaises(TypeError):
            self.rec.x = "2"
        with self.assertRaises(ValueError):
            self.rec.x = -1

    def test_y_setter(self):
        """
        testing the y setter
        """
        with self.assertRaises(TypeError):
            self.rec.y = "2"
        with self.assertRaises(ValueError):
            self.rec.y = -1


if __name__ == '__main__':
    unittest.main()
