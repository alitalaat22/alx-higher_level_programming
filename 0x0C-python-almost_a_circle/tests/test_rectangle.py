# #!/usr/bin/python3
"""jdjfgjfghjfghjf"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        """ إعداد البيانات الأساسية لكل اختبار """
        self.rect1 = Rectangle(10, 2, 1, 9)
        self.rect2 = Rectangle(5, 7)
        self.rect3 = Rectangle(3, 4, 2, 1, 12)

    def test_initialization(self):
        """ اختبار التهيئة الصحيحة للخصائص """
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect1.x, 1)
        self.assertEqual(self.rect1.y, 9)
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect2.width, 5)
        self.assertEqual(self.rect2.height, 7)
        self.assertEqual(self.rect2.x, 0)
        self.assertEqual(self.rect2.y, 0)
        self.assertEqual(self.rect2.id, 2)
        self.assertEqual(self.rect3.id, 12)

    def test_width_setter(self):
        """ اختبار تعيين عرض المستطيل """
        self.rect1.width = 15
        self.assertEqual(self.rect1.width, 15)
        with self.assertRaises(ValueError):
            self.rect1.width = -5
        with self.assertRaises(TypeError):
            self.rect1.width = "a"

    def test_height_setter(self):
        """ اختبار تعيين ارتفاع المستطيل """
        self.rect1.height = 8
        self.assertEqual(self.rect1.height, 8)
        with self.assertRaises(ValueError):
            self.rect1.height = -3
        with self.assertRaises(TypeError):
            self.rect1.height = "b"

    def test_x_setter(self):
        """ اختبار تعيين الإحداثي x """
        self.rect1.x = 5
        self.assertEqual(self.rect1.x, 5)
        with self.assertRaises(ValueError):
            self.rect1.x = -1
        with self.assertRaises(TypeError):
            self.rect1.x = 1.5

    def test_y_setter(self):
        """ اختبار تعيين الإحداثي y """
        self.rect1.y = 4
        self.assertEqual(self.rect1.y, 4)
        with self.assertRaises(ValueError):
            self.rect1.y = -2
        with self.assertRaises(TypeError):
            self.rect1.y = 2.5

    def test_area(self):
        """ اختبار حساب المساحة """
        self.assertEqual(self.rect1.area(), 20)
        self.assertEqual(self.rect2.area(), 35)

    def test_display(self):
        """ اختبار طريقة العرض """
        with self.assertLogs('sys.stdout', level='INFO') as log:
            self.rect1.display()
            self.assertIn(" " * 1 + "#" * 10, log.output[0])
            self.assertIn("\n" * 9 + " " * 1 + "#" * 10, log.output[1])

    def test_str(self):
        """ اختبار تحويل الكائن إلى سلسلة نصية """
        self.assertEqual(str(self.rect1), "[Rectangle] (1) 1/9 - 10/2")

    def test_update_args(self):
        """ اختبار تحديث الخصائص باستخدام معلمات الموضع """
        self.rect1.update(5, 6, 7, 8, 9)
        self.assertEqual(self.rect1.id, 5)
        self.assertEqual(self.rect1.width, 6)
        self.assertEqual(self.rect1.height, 7)
        self.assertEqual(self.rect1.x, 8)
        self.assertEqual(self.rect1.y, 9)

    def test_update_kwargs(self):
        """ اختبار تحديث الخصائص باستخدام معلمات المفاتيح """
        self.rect1.update(width=15, height=10, x=3, y=4)
        self.assertEqual(self.rect1.width, 15)
        self.assertEqual(self.rect1.height, 10)
        self.assertEqual(self.rect1.x, 3)
        self.assertEqual(self.rect1.y, 4)

    def test_to_dictionary(self):
        """ اختبار تحويل الكائن إلى قاموس """
        self.assertEqual(self.rect1.to_dictionary(), {
            'id': 1,
            'width': 10,
            'height': 2,
            'x': 1,
            'y': 9
        })

if __name__ == '__main__':
    unittest.main()
