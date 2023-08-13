#!/usr/bin/python3
"""entry point of the command interpreter:"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
