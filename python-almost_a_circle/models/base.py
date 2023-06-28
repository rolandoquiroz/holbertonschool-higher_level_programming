#!/usr/bin/python3
"""
module class Base

"""
import json
import csv
import turtle
import random


class Base:
    """
    class Base

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize instance attributes

        Args:
            id (int): object id

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        json string representation
        of list_dictionaries

        """
        if ((list_dictionaries is None) or (len(list_dictionaries) == 0)):
            return("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list_objs to a file

        """
        filename = "{:s}.json".format(cls.__name__)

        if list_objs is None:
            with open(filename, mode='w+', encoding='utf-8') as f:
                f.write(cls.to_json_string([]))
        else:
            with open(filename, mode='w+', encoding='utf-8') as f:
                f.write(cls.to_json_string([i.to_dictionary()
                                            for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the JSON
        string representation json_string

        """
        if ((json_string is None) or (len(json_string) == 0)):
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        This method returns an instance
        with all attributes already set

        """
        if cls.__name__ is "Rectangle":
            tmp = cls(1, 1)
        if cls.__name__ is "Square":
            tmp = cls(1)
        tmp.update(**dictionary)
        return (tmp)

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances.

        """
        lst = []
        filename = "{:s}.json".format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                inss = cls.from_json_string(f.read())
            for ins in inss:
                lst.append(cls.create(**ins))
            return (lst)
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This method encodes to CSV file.

        """
        if (list_objs is None):
            list_objs = []
        if (cls.__name__ == "Rectangle"):
            Attr = ["id", "width", "height", "x", "y"]
        if (cls.__name__ == "Square"):
            Attr = ["id", "size", "x", "y"]
        with open("{:s}.csv".format(cls.__name__),
                  mode='w+', encoding='utf-8') as f:
            writer = csv.DictWriter(f, Attr)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        This merhod decodes CSV
        file to object list

        """
        obj_list = []
        with open(cls.__name__ + ".csv", "r", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tmp = {}
                for key, value in dict(row).items():
                    tmp[key] = int(value)
                obj_list.append(cls.create(**tmp))
        return (obj_list)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares

        """
        colours = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
        ninja_turtle = turtle.Turtle()

        for r in list_rectangles:
            ninja_turtle.setpos(r.x, r.y)
            ninja_turtle.pencolor(random.choice(colours))
            ninja_turtle.pendown()
            ninja_turtle.showturtle()
            ninja_turtle.forward(r.width)
            ninja_turtle.left(90)
            ninja_turtle.forward(r.height)
            ninja_turtle.left(90)
            ninja_turtle.forward(r.width)
            ninja_turtle.left(90)
            ninja_turtle.forward(r.height)
            ninja_turtle.left(90)
            ninja_turtle.hideturtle()
            ninja_turtle.penup()
        ninja_turtle.setpos(0, 0)

        for s in list_squares:
            ninja_turtle.setpos(s.x, s.y)
            ninja_turtle.pencolor(random.choice(colours))
            ninja_turtle.pendown()
            ninja_turtle.showturtle()
            for i in range(4):
                ninja_turtle.forward(s.size)
                ninja_turtle.left(90)
            ninja_turtle.hideturtle()
            ninja_turtle.penup()
        ninja_turtle.setpos(0, 0)
