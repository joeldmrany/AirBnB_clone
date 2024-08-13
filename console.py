#!/usr/bin/python3
"""
That is the start of hbnb project
and that is console
"""
import cmd


class console(cmd.Cmd):
    """that is start of cmd console"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        write [quit] to get out from console
        """
        return True

    def do_EOF(self, line):
        """
        you can end console with EOF
        """
        return True


if __name__ == '__main__':
    console().cmdloop()
