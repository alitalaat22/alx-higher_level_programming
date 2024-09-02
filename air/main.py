#!/usr/bin/python3
# BaseGeometry = __import__('in').BaseGeometry

# bg = BaseGeometry()

# bg.integer_validator("my_int", 12)
# bg.integer_validator("width", 89)

# try:
#     bg.integer_validator("name", "John")
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("age", 0)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("distance", -4)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# """--------------------------------------"""

#!/usr/bin/python3
Rectangle = __import__('in').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

"@@@@@@@@@@@@@@@@@@@@@@@ 9. Full rectangle@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

#!/usr/bin/python3
# Rectangle = __import__('in').Rectangle

# r = Rectangle(3, 5)

# print(r)
# print(r.area())

print("---------------------------------------10 Square---------------------------------------")
Square = __import__('in').Square

s = Square(13)

print(s)
print(s.area())
