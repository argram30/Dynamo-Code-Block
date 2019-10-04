import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('DSCoreNodes')
from DSCore import *

number_of_colors = IN[0]

# Generate hex colors randomly
# color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]


# This method shuffles the colors with in the list
def random_color1():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	color = Color.ByARGB(255,r,g,b)
	return color


OUT = [random_color() for i in range(number_of_colors)]