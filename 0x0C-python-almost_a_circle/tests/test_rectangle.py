#!/usr/bin/python3
""" test for rectangle module"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
from contextlib import redirect_stdout


class Test_rectangle(unittest.TestCase):
    """testing for rectangle class"""

    def test_init(self):
        """testing for rectangle class initialize"""
        obj1 = Rectangle(10, 2)
        obj2 = Rectangle(2, 10, 7, 6)
        self.assertEqual(obj1.id, obj2.id - 1)
        self.assertEqual(obj2.id, obj1.id + 1)

        obj3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(obj3.id, 12)

        obj4 = Rectangle(10, 2, 7)
        self.assertEqual(obj4.id, obj1.id + 2)

        obj5 = Rectangle(4, 10)
        self.assertEqual(obj5.id, obj4.id + 1)

        obj6 = Rectangle(10, 2, 0, 0, 15)
        self.assertEqual(obj6.id, 15)

        obj7 = Rectangle(4, 10, 3)
        self.assertEqual(obj7.id, obj5.id + 1)

    def test_widthsetandget(self):
        """testing for rectangle class width"""
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(ValueError, Rectangle, -10, 2)

    def test_heightsetandget(self):
        """testing for rectangle class height"""
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, 10, -2)

    def test_xsetandget(self):
        """testing for rectangle class x"""
        self.assertRaises(TypeError, Rectangle, 10, 2, {})
        self.assertRaises(ValueError, Rectangle, 10, 2, -3, 2)

    def test_ysetandget(self):
        """testing for rectangle class y"""
        self.assertRaises(TypeError, Rectangle, 10, 2, 4, {})
        self.assertRaises(ValueError, Rectangle, 10, 2, 5, -3)

    def test_area(self):
        """testing for rectangle class area"""
        obj8 = Rectangle(3, 2)
        self.assertEqual(obj8.area(), 6)

        obj9 = Rectangle(2, 10)
        self.assertEqual(obj9.area(), 20)

        obj10 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(obj10.area(), 56)

    def test_display(self):
        """testing for rectangle class display"""
        obj11 = Rectangle(3, 2)
        outr11 = StringIO()
        with redirect_stdout(outr11):
            obj11.display()
            self.assertEqual(outr11.getvalue(), "###\n###\n")

        obj12 = Rectangle(2, 1)
        outr12 = StringIO()
        with redirect_stdout(outr12):
            obj12.display()
            self.assertEqual(outr12.getvalue(), "##\n")

    def test_string(self):
        """testing for rectangle class string"""
        obj13 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(obj13.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        obj14 = Rectangle(5, 5, 1)
        self.assertEqual(obj14.__str__(), "[Rectangle] (21) 1/0 - 5/5")

    def test_display2(self):
        """testing for rectangle class display"""
        obj15 = Rectangle(2, 3, 2, 2)
        outr15 = StringIO()
        with redirect_stdout(outr15):
            obj15.display()
            self.assertEqual(outr15.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        obj16 = Rectangle(3, 2, 1, 0)
        outr16 = StringIO()
        with redirect_stdout(outr16):
            obj16.display()
            self.assertEqual(outr16.getvalue(), " ###\n ###\n")

    def test_update(self):
        """testing for rectangle class update"""
        obj17 = Rectangle(89, 2, 3, 4, 5)
        obj17.update(83)
        self.assertEqual(obj17.__str__(), "[Rectangle] (83) 3/4 - 89/2")
        obj17.update(83, 5)
        self.assertEqual(obj17.__str__(), "[Rectangle] (83) 3/4 - 5/2")

    def test_update2(self):
        """testing for rectangle class update"""
        obj18 = Rectangle(10, 10, 10, 10, 15)
        obj18.update(width=1, x=2)
        self.assertEqual(obj18.__str__(), "[Rectangle] (15) 2/10 - 1/10")
        obj18.update(x=1, height=2, y=3, width=4)
        self.assertEqual(obj18.__str__(), "[Rectangle] (15) 1/3 - 4/2")


if __name__ == "__main__":
    unittest.main()
