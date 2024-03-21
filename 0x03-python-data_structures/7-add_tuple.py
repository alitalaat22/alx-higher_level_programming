#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    
    # إضافة قيمة صفرية إذا كانت الترتيبات أقل من عنصرين
    if len_a < 2:
        tuple_a += (0,)
    if len_b < 2:
        tuple_b += (0,)
    
    # جمع العناصر المتوافقة من الترتيبات
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1] if len_a > 1 and len_b > 1 else 0

    # إرجاع ترتيب جديد بالمجموعات
    return (sum_1, sum_2)
