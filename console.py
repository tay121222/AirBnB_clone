#!/usr/bin/python3
"""entry point of the command interpreter:"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter """
    prompt = "(hbnb) "

    def parse_dictionary(self, command):
        try:
            parts = command.split('(')
            id_and_dict = parts[1][:-1]
            id_str, dict_str = id_and_dict.split(', ', 1)
            return id_str[1:-1], eval(dict_str)
        except Exception:
            return None

    def onecmd(self, line):
        """Class to allow the format <class name>.all()"""

        if line == "quit":
            return True
        parts = line.split('.')
        if len(parts) == 2:
            class_name, command = parts
            if class_name in storage.classes():
                if command == "all()":
                    instances = storage.all()
                    print(
                            [str(instance) for instance in instances.values()
                                if instance.__class__.__name__ == class_name]
                            )
                elif command == 'count()':
                    instances = storage.all()
                    count = len(
                            [instance for instance in instances.values()
                                if instance.__class__.__name__ == class_name]
                            )
                    print(count)
                elif command.startswith('show("') and command.endswith('")'):
                    id_str = command[6:-2]
                    instances = storage.all()
                    key = "{}.{}".format(class_name, id_str)
                    if key in instances:
                        print(instances[key])
                    else:
                        print("** no instance found **")
                elif command.startswith(
                        'destroy("'
                        ) and command.endswith('")'):
                    id_str = command[9:-2]
                    instances = storage.all()
                    key = "{}.{}".format(class_name, id_str)
                    if key in instances:
                        del instances[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                elif command.startswith('update("') and command.endswith('")'):
                    parts = command.split(', ')
                    if len(parts) != 3:
                        return
                    id_str = parts[0][8:-1]
                    attribute_name = parts[1][1:-1]
                    attribute_value = parts[2][1:-2]
                    instances = storage.all()
                    key = "{}.{}".format(class_name, id_str)
                    if key in instances:
                        instance = instances[key]
                        setattr(instance, attribute_name, attribute_value)
                        instance.save()
                    else:
                        print("** no instance found **")
                elif command.startswith('update("') and command.endswith('})'):
                    id_str, dictionary = self.parse_dictionary(command)
                    if id_str is not None:
                        instances = storage.all()
                        key = "{}.{}".format(class_name, id_str)
                        if key in instances:
                            instance = instances[key]
                            for attr_name, attr_value in dictionary.items():
                                setattr(instance, attr_name, attr_value)
                            instance.save()
                        else:
                            print("** no instance found **")
                    else:
                        print(
                                "** Unknown syntax: {}.{} **"
                                .format(class_name, command)
                                )
            else:
                print("** class doesn't exist **")
        else:
            super().onecmd(line)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        args = arg.split()
        if args and args[0] in storage.classes():
            instances = storage.all()
            class_name = args[0]
            print(
                    [str(instance) for instance in instances.values()
                        if instance.__class__.__name__ == class_name]
                    )
        elif not args:
            instances = storage.all()
            print([str(instances[key]) for key in instances])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                instance = instances[key]
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    setattr(instance, attr_name, args[3])
                    instance.save()
            else:
                print("** no instance found **")

    def do_create(self, arg):
        """Create new instance of User"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Print String Representation"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
