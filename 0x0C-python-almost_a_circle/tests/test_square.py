#!/usr/bin/python3
"""jgf jdfgjdfjg djdgj d
fgudfghdfghfdghsrhgsf"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    
    def setUp(self):
        """ إعداد البيانات الأساسية لكل اختبار """
        self.square1 = Square(5, 2, 3)
        self.square2 = Square(8)
        self.square3 = Square(4, 1, 1, 12)

    def test_initialization(self):
        """ اختبار التهيئة الصحيحة للخصائص """
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square1.x, 2)
        self.assertEqual(self.square1.y, 3)
        self.assertEqual(self.square1.id, 1)
        self.assertEqual(self.square2.size, 8)
        self.assertEqual(self.square2.x, 0)
        self.assertEqual(self.square2.y, 0)
        self.assertEqual(self.square2.id, 2)
        self.assertEqual(self.square3.id, 12)

    def test_size_setter(self):
        """ اختبار تعيين حجم المربع """
        self.square1.size = 10
        self.assertEqual(self.square1.size, 10)
        self.assertEqual(self.square1.width, 10)
        self.assertEqual(self.square1.height, 10)
        with self.assertRaises(ValueError):
            self.square1.size = -5
        with self.assertRaises(TypeError):
            self.square1.size = "a"

    def test_update_args(self):
        """ اختبار تحديث الخصائص باستخدام معلمات الموضع """
        self.square1.update(5, 6, 7, 8)
        self.assertEqual(self.square1.id, 5)
        self.assertEqual(self.square1.size, 6)
        self.assertEqual(self.square1.x, 7)
        self.assertEqual(self.square1.y, 8)

    def test_update_kwargs(self):
        """ اختبار تحديث الخصائص باستخدام معلمات المفاتيح """
        self.square1.update(size=15, x=3, y=4)
        self.assertEqual(self.square1.size, 15)
        self.assertEqual(self.square1.x, 3)
        self.assertEqual(self.square1.y, 4)

    def test_str(self):
        """ اختبار تحويل الكائن إلى سلسلة نصية """
        self.assertEqual(str(self.square1), "[Square] (1) 2/3 - 5")

    def test_to_dictionary(self):
        """ اختبار تحويل الكائن إلى قاموس """
        self.assertEqual(self.square1.to_dictionary(), {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        })

if __name__ == '__main__':
    unittest.main()
