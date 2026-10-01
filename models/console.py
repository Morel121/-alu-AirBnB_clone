#!/usr/bin/python3
"""
Console Module
Entry point for the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class containing the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
