#!/usr/bin/python3
"""
command line interpreter for python project airbnb
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class which defines the command line 
    interpreter behavior for the AirBnB project
    """
    intro = "AirBnB console"
    prompt = "(hbnb) "
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]

    def do_create(self, string):
        """A method that creates an instance of the BaseModel class"""
        if not string:
            print("** class name missing **")
        elif string not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            temp_obj = BaseModel()
            storage.save()
            print(temp_obj.id)

    def help_create(self):
        """A method that creates an instance of the BaseModel class"""
        print("Command that creates a new instance of the class BaseModel")

    def do_show(self, string):
        """A method that prints the string representation of an object with a given ID"""
        parsed_string = string.split()
        all_dict = storage.all()

        try:
            name = parsed_string[0] if len(parsed_string) >= 1 else None
            id = parsed_string[1] if len(parsed_string) >= 2 else None
        except IndexError:
            pass

        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(parsed_string[0], parsed_string[1])
            if key in all_dict:
                print(all_dict[key].__str__())
            else:
                print("** no instance found **")

    def do_destroy(self, string):
        """A method that prints the string representation of an object with a given ID"""
        parsed_string = string.split()
        all_dict = storage.all()

        try:
            name = parsed_string[0] if len(parsed_string) >= 1 else None
            id = parsed_string[1] if len(parsed_string) >= 2 else None
        except IndexError:
            pass

        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(name, id)
            if key in all_dict:
                del all_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, string):
        """A method that prints all string representation of all instances based on the argument string provided"""
        parse_string = string.split()
        all_dict = storage.all()
        list_obj = []

        if len(parse_string) == 0:
            for key, value in all_dict.items():
                list_obj.append(str(value.__str__()))
            print(list_obj)
        elif len(parse_string) == 1:
            class_name = parse_string[0]
            if class_name in self.classes:
                for key, value in all_dict.items():
                    if class_name == value.__class__.__name__:
                        list_obj.append(all_dict[key].__str__())
                print(list_obj)
            else:
                print("** class doesn't exist **")

    def do_update(self, string):
        """A method that updates an instance with a particular attribute,
        given information about id, attribute value and attribute name"""
        parsed_string = string.split()
        all_dict = storage.all()
        forbidden_atts = ["id", "created_at", "updated_at"]

        if len(parsed_string) > 4:
            parsed_string = parsed_string[:4]

        try:
            name = parsed_string[0] if len(parsed_string) >= 1 else None
            id = parsed_string[1] if len(parsed_string) >= 2 else None
            attribute_name = parsed_string[2] if len(parsed_string) >= 3 \
            else None
            attribute_value = parsed_string[3] if len(parsed_string) >= 4 \
            else None
        except IndexError:
            pass
        
        if not name:
            print("** class name missing **")
        elif name not in self.classes:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        elif not attribute_name:
            print("** attribute name missing **")
        elif not attribute_value:
            print("** value missing **")
        else:
            key_temp = "{}.{}".format(name, id)
            if key_temp in all_dict:
                for key, value in all_dict.items():
                    if id == value.id:
                        if attribute_name in forbidden_atts:
                            pass
                        else:
                            setattr(all_dict[key], attribute_name, eval(attribute_value))
                            storage.save()
            else:
                print("** no instance found **")

    def do_EOF(self, line):
        """A method that exits the cmd by returning exit"""
        return True

    def help_EOF(self):
        """A method that exits the cmd by returning exit"""
        print("EOF command exits the command line")

    def do_quit(self, line):
        """A method that exits the cmd by returning exit"""
        return True

    def help_quit(self):
        """A method that exits the cmd by returning exit"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Method which controls behavior of the command 
        line when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
