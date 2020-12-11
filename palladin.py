#! /usr/bin/env python

import os, shutil, subprocess

from colorama import Fore, Style

class Palladin:
    def __init__(self):
        self.config = os.path.expanduser("~/.config/")
        self.mercy  = ["palladin"]

        if not os.path.exists(self.config + "palladin"):
            os.mkdir(self.config + "palladin")

        try:
            with open(self.config + "palladin/mercy.list") as f:
                for name in f:
                    self.mercy.append(name.rstrip())
        except FileNotFoundError:
            pass

    def inspect(self):
        suspicious = lambda x: subprocess.run(("which", x), capture_output=True).returncode
        slain = 0

        try:
            for name in os.listdir(self.config):
                if suspicious(name) and name not in self.mercy:
                    print("My lord, I have found a suspicious one - " + color(Fore.YELLOW, name))
                    choice = input("Shall I slay him? (y/[n]): ")
                    if choice == "y":
                        self.slay(name)
                        slain += 1
                        negative(color(Fore.RED, "As you wish, my lord."))
                    else:
                        positive(color(Fore.GREEN, "I admire your grace, my lord!"))
                        choice = input("Shall I save him forever? (y/[n]): ")
                        if choice == "y":
                            self.remember(name)
                            positive(color(Fore.GREEN, "He will be safe."))
                        else:
                            negative(color(Fore.RED, "If we meet again, he will know my wrath!"))
        except KeyboardInterrupt:
            negative("\nMy work is done if you think so, my lord:", Palladin.report(slain))
        else:
            positive("My work is done, my lord:", Palladin.report(slain))

    def slay(self, name):
        if os.path.isdir(self.config + name):
            shutil.rmtree(self.config + name)
        else:
            os.remove(self.config + name)

    def remember(self, name):
        with open(self.config + "palladin/mercy.list", "a") as f:
            f.write(name + "\n")

    def report(slain):
        return (str(slain) if slain else "no") + (" enemy was" if slain == 1 else " enemies were") + " slain."

color = lambda c, x: c + x + Style.RESET_ALL

def positive(*args):
    colored = (color(Fore.GREEN, arg) for arg in args)
    print(*colored)

def negative(*args):
    colored = (color(Fore.RED, arg) for arg in args)
    print(*colored)

if __name__ == "__main__":
    try:
        Palladin().inspect()
    except KeyboardInterrupt:
        print("\nMy work is done if you think so, my lord.")
