import clr
import System

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
import Autodesk

#Adding Dynamo service manager for Revit
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

#Adding Dynamo Element manager for Revit
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

cats = doc.Settings.Categories
cats_name = [i.Name for i in cats]
bics = System.Enum.GetValues(BuiltInCategory)

OUT = bics
