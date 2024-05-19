#!/usr/bin/python3
"""This module contains the console.py module"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import strge
import cmd
import os
import re


def tokenize(arg: str) -> list:
    """ Splits a string into tks delimited by space

    Args:
        arg (string): strings to be splitted

    Returns:
        list: list of strings
    """
    token = re.split(r"[ .(),]", arg)
    return token


class HBNBCommand(cmd.Cmd):
    """The class HBNB that builds a console"""

    prompt = "(hbnb) "
    CLSNMES = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg: str) -> bool:
        """Quit command to exit the program"""

        return True

    def default(self, arg):
        """Default method"""

        fdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        tks = tokenize(arg)
        for key in fdict.keys():
            # checking for commands to call
            if key == tks[1]:
                # for if args is parentheses eg("something")
                if tks[2] != "" and len(tks) < 6:
                    # print(tks)
                    sparg = tks[2].replace('"', '')
                    args = "{} {}".format(tks[0], sparg)
                    return fdict[tks[1]](args)
                elif len(tks) > 6:
                    # for update version 1
                    # print(tks)
                    ar1 = tks[2].replace('"', '')
                    ar2 = tks[4].replace('"', '')
                    ar3 = tks[6].replace('"', '')
                    args = "{} {} {} {}".format(tks[0], ar1, ar2, ar3)
                    # print(args)
                    return fdict[tks[1]](args)

                else:
                    # print(tks)
                    return fdict[tks[1]](tks[0])

        # print(tks)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg: str) -> None:
        """Creates a new instance"""

        tks = tokenize(arg)
        if arg == "":
            print("** class name missing **")
        elif tks[0] not in HBNBCommand.CLSNMES:
            print("** class doesn't exist **")
        else:
            print(eval(tks[0])().id)
            strge.save()

    def do_clear(self, args: str) -> None:
        """Clear the screen"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def do_show(self, arg: str) -> None:
        """prints the string representation of an instance"""

        tks = tokenize(arg)
        if arg == "":
            print("** class name missing **")
        elif tks[0] not in HBNBCommand.CLSNMES:
            print("** class doesn't exist **")
        elif len(tks) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tks[0], tks[1])
            if key not in strge.all():
                print("** no instance found **")
            else:
                print(strge.all()[key])

    def do_destroy(self, arg: str) -> None:
        """Deletes an instance based on the class name and id"""

        tks = tokenize(arg)
        if arg == "":
            print("** class name missing **")
        elif tks[0] not in HBNBCommand.CLSNMES:
            print("** class doesn't exist **")
        elif len(tks) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tks[0], tks[1])
            if key not in strge.all():
                print("** no instance found **")
            else:
                del strge.all()[key]
                strge.save()

    def do_all(self, arg: str) -> None:
        """Prints all string representation of all instances"""

        tks = tokenize(arg)
        if arg == "":
            print([str(value) for value in strge.all().values()])
        elif tks[0] not in HBNBCommand.CLSNMES:
            print("** class doesn't exist **")
        else:
            temp = [str(v) for k, v in strge.all().items()
                    if tks[0] in k]
            print(temp)

    def do_update(self, arg: str) -> None:
        """ Updates the class"""
        tks = tokenize(arg)
        objson = strge.all()
        if arg == "":
            # print(tks)
            print("** class name missing **")
            return False
        elif tks[0] not in HBNBCommand.CLSNMES:
            # print(tks)
            print("** class doesn't exist **")
            return False
        elif len(tks) < 2:
            # print(tks)
            print("** instance id missing **")
            return False

        elif "{}.{}".format(tks[0], tks[1]) not in objson.keys():
            # print(tks)
            print("** no instance found **")
            return False
        elif len(tks) < 3:
            # print(tks)
            print("** attribute name missing **")
            return False
        elif len(tks) == 3:
            try:
                type(eval(tks[2])) != dict
            except NameError:
                # print(tks)
                print("** value missing **")
                return False

        if len(tks) > 3:
            obj = objson["{}.{}".format(tks[0], tks[1])]
            if tks[2] in obj.__class__.__dict__.keys():
                # get the attribute value type for typecast
                vtype = type(obj.__class__.__dict__[tks[2]])
                obj.__dict__[tks[2]] = vtype(tks[3])
            else:
                obj.__dict__[tks[2]] = tks[3]

        elif type(eval(tks[2])) == dict:
            obj = objson["{}.{}".format(tks[0], tks[1])]
            for k, v in eval(tks[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in [str, int, float]):
                    vtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = vtype(v)
                else:
                    obj.__dict__[k] = v

        strge.save()

    def do_count(self, arg):
        """counts"""

        tk = tokenize(arg)
        # set counter
        ct = 0
        # get all object keys
        objk = strge.all().keys()
        for key in objk:
            if tk[0] in key:
                ct += 1
        print(ct)

    def do_EOF(self, arg):
        """Handles EOF"""

        raise systemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
