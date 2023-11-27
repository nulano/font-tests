import os

from fontTools import ttx

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    os.remove("EBDTTestFont.ttf")
except OSError:
    pass

ttx.main(["EBDTTestFont.ttx"])
