#For Iron Python clr should be added to link the dll libraries
import clr

#Importing DS Geometry Nodes - Geometry Libraries from Design script could be used in python
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#Importing DSCore Nodes - Colors, Lists everything from Design script could be used in python
clr.AddReference('DSCoreNodes')
from DSCore import *

#Import Dynamo Dictionary in to Iron python
clr.AddReference("DesignScriptBuiltin")
from DesignScript.Builtin import Dictionary
OUT = Dictionary.ByKeysValues(["A"], [1,3])
