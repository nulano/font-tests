import os

from fontTools import ttx

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    os.remove("CBDTTestFont.ttf")
except OSError:
    pass

ttx.main(["CBDTTestFont.ttx"])
