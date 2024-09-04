#!/usr/bin/python3
"""test for model/base.py"""
import unittest
import os
import json
import csv
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    
    def setUp(self):
        """ إعداد البيانات الأساسية لكل اختبار """
        self.rect1 = Rectangle(10, 2, 1, 9)
        self.rect2 = Rectangle(5, 7)
        self.sq1 = Square(10, 2, 1)
        self.sq2 = Square(5)

    def test_to_json_string(self):
        """ اختبار تحويل قائمة القواميس إلى JSON """
        list_dict = [self.rect1.to_dictionary(), self.rect2.to_dictionary()]
        json_string = Base.to_json_string(list_dict)
        expected = json.dumps(list_dict)
        self.assertEqual(json_string, expected)

    def test_from_json_string(self):
        """ اختبار تحويل JSON إلى قائمة قواميس """
        list_dict = [self.rect1.to_dictionary(), self.rect2.to_dictionary()]
        json_string = json.dumps(list_dict)
        list_output = Base.from_json_string(json_string)
        self.assertEqual(list_output, list_dict)

    def test_save_to_file(self):
        """ اختبار حفظ إلى ملف JSON """
        list_objs = [self.rect1, self.rect2]
        Base.save_to_file(list_objs)
        filename = 'Base.json'
        with open(filename, 'r') as file:
            content = file.read()
            list_dict = [self.rect1.to_dictionary(), self.rect2.to_dictionary()]
            expected = Base.to_json_string(list_dict)
            self.assertEqual(content, expected)
        os.remove(filename)

    def test_load_from_file(self):
        """ اختبار تحميل من ملف JSON """
        list_objs = [self.rect1, self.rect2]
        Base.save_to_file(list_objs)
        list_loaded = Base.load_from_file()
        self.assertEqual(len(list_loaded), 2)
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in list_loaded))
        os.remove('Base.json')

    def test_save_to_file_csv(self):
        """ اختبار حفظ إلى ملف CSV """
        list_objs = [self.rect1, self.rect2]
        Base.save_to_file_csv(list_objs)
        filename = 'Base.csv'
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            list_dict = [self.rect1.to_dictionary(), self.rect2.to_dictionary()]
            records = ['id', 'width', 'height', 'x', 'y']
            reader_dicts = [dict(row) for row in reader]
            list_dicts = [{k: int(v) for k, v in d.items()} for d in reader_dicts]
            self.assertEqual(list_dicts, list_dict)
        os.remove(filename)

    def test_load_from_file_csv(self):
        """ اختبار تحميل من ملف CSV """
        list_objs = [self.rect1, self.rect2]
        Base.save_to_file_csv(list_objs)
        list_loaded = Base.load_from_file_csv()
        self.assertEqual(len(list_loaded), 2)
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in list_loaded))
        os.remove('Base.csv')

    def test_draw(self):
        """ اختبار رسم باستخدام مكتبة turtle """
        try:
            Base.draw([self.rect1], [self.sq1])
        except turtle.TurtleGraphicsError:
            self.fail("TurtleGraphicsError raised during draw")

if __name__ == '__main__':
    unittest.main()
