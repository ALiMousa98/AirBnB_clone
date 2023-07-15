#!/usr/bin/python3
""" Console Class  """
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        if self.file:
            self.file.close()
            self.file = None
        return True

    def do_EOF(self, arg):
        """Exit command to exit the program
        """
        if self.file:
            self.file.close()
            self.file = None

        return True

    def do_create(self, line):
        """This creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        else:
            paras = line.split(" ")
            if paras[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(paras) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(paras[0], paras[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        else:
            paras = line.split(" ")
            if paras[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(paras) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(paras[0], paras[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """This creates an instance.
        """
        if line == "" or line is None:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            nl = [str(obj) for key, obj in storage.all().items()
                  if type(obj).__name__ == line]
            print(nl)

    def do_update(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        else:
            paras = line.split(" ")
            if paras[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(paras) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(paras[0], paras[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    if len(paras) == 2:
                        print("** attribute name missing **")
                    #elif paras[2] not in storage.all()[key].to_dict().keys():
                        #print()
                    else:
                        if len(paras) == 3:
                            print("** value missing **")
                        else:
                            attributes = storage.attributes()[paras[0]]
                            for attribute in attributes:
                                if attribute == paras[2]:
                                    setattr(storage.all()[key], attribute,
                                            type(storage.all()[key].to_dict()[attribute])(value))
                            storage.all()[key].save()


"""def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))
"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
