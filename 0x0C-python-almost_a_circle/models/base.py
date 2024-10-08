#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project"""


import turtle
import json
import os
import csv


class Base:
    """this a main class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this method assig id for  nb obj"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """thisfjjf;l
        asjdfklja;ldkfkajfla"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """thsofjklasjf
        f;ladsfjlkjaf;lk;"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                s = []
                for obj in list_objs:
                    s.append(obj.to_dictionary())

                f.write(cls.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create new instance method"""
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            new_inst = cls(1)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """Load list of instances from JSON file"""
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []

        with open(filename, "r") as f:
            json_string = f.read()

        dictionaries = cls.from_json_string(json_string)
        instances = [cls.create(**d) for d in dictionaries]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and saves to file"""

        # if (type(list_objs) != list and list_objs is not None
        #    or not all(isinstance(i, cls) for i in list_objs)):

        #     raise TypeError("list_objs must be a list of instances")

        # file_name = cls.__name__ + ".csv"
        # with open(file_name, 'w') as my_file:
        #     if list_objs is not None:
        #         list_objs = [i.todictionary for i in list_objs]
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         script = csv.DictWriter(my_file, fieldnames=records)
        #         script.writeheader()
        #         script.writerows(list_objs)

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""

        # file_name = cls.__name__ + ".csv"
        # list_of_instances = []
        # if os.path.exists(file_name):
        #     with open(file_name, 'r') as my_file:
        #         reader = csv.reader(my_file, delimiter=',')
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         for i, row in enumerate(reader):
        #             if i > 0:
        #                 x = cls(1, 1)
        #                 for j, y in enumerate(row):
        #                     if y:
        #                         setattr(x, records[j], int(y))
        #                 list_of_instances.append(x)
        # return list_of_instances

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
