#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        if self.file:
            self.file.close()
            self.file = None
        return True

    def do_EOF(self, arg):
        '''Exit command to exit the program
        '''
        if self.file:
            self.file.close()
            self.file = None
        return True


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
