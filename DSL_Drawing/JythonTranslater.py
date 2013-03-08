import Translater
import math
from turtle import turtle

class Jtrans(Translater):
    def __init__(self):
        pass

    def actionPerformed(self, event):
        self.t.parseCode()

    def setDYPL( self, obj ):
        print("Got a DYPL instance: ")
        self.t = turtle(obj)


if __name__ == '__main__':
    import DYPL
    DYPL(Jtrans())
