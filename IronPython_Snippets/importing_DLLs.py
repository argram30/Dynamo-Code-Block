import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from System.Collections.Generic import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Analysis import *

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

collector = Autodesk.Revit.DB.FilteredElementCollector(doc)
linkInstances = collector.OfClass(Autodesk.Revit.DB.RevitLinkInstance)

linkDoc, linkName, linkInstId = [], [], []
for i in linkInstances:
	linkDoc.append(i.GetLinkDocument())
	linkName.append(i.Name)
	linkInstId.append(i.Id)

OUT = linkDoc, linkName, linkInstances, linkInstId