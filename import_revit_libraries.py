#importing Geometry Libraries from Designscript
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#Importing Document Manager and Transaction Manager
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#Importing generics Library from the OS
from System.Collections.Generic import *

#Import Revit API
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Analysis import *

doc = DocumentManager.Instance.CurrentDBDocument
uiApp = DocumentManager.Instance.CurrentUIApplication
app = uiApp.Application

#Import toDSType(bool) extension method
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

#Importing Revit APIUI
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import TextBox
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import TaskDialogCommonButtons

#A small snippet to access the elements from Revit Database
collector = Autodesk.Revit.DB.FilteredElementCollector(doc)
levels = collector.OfClass(Level)

#Converting an item in to Lists
def convertToList(testList):
	if isinstance(testList, list):
		return testList
	else:
		return [testList]
