#!/usr/bin/python3
"""this module"""


def class_to_json(obj):
    """إرجاع وصف القاموس مع البنية البسيطة للبيانات من أجل تسلسل JSON لكائن."""
    return obj.__dict__
