#from post https://forum.dynamobim.com/t/collect-all-categories-in-a-project/6054/18
import clr
import System
from System.Collections.Generic import *

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
import Autodesk

#Adding Dynamo Element manager for Revit
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

#Adding Dynamo service manager for Revit
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

builtInCats = List[BuiltInCategory]()
builtInCats.Add(BuiltInCategory.OST_Doors)
builtInCats.Add(BuiltInCategory.OST_Windows)

 
filter1 = ElementMulticategoryFilter(builtInCats)

elements = FilteredElementCollector(doc).WherePasses(filter1).ToElements()

OUT = elements