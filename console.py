#!/usr/bin/python3
"""
That is the start of hbnb project
and that is console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """that is start of cmd console"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        you can end console with EOF
        """
        return True

    def emptyline(self):
        """
        Override the emptyline method to do nothing
        when an empty line + ENTER is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
