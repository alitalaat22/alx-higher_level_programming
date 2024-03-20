#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i, n in enumerate(r):  # استخدام enumerate للحصول على فهرس العناصر
            print("{}".format(n), end='')
            if i != len(r) - 1:  # التأكد من أنه ليس آخر عنصر في الصف
                print(" ", end='')  # طباعة مسافة فقط إذا لم يكن هذا آخر عنصر في الصف
        else:
            print()  # طباعة سطر فارغ بعد كل صف
