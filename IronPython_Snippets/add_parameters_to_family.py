import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

from System.Collections.Generic import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *
import System

dataEnteringNode = Instance

para_Name = IN[0]
exec("para_Type = ParameterType.%s" % IN[1])
exec("param_Group = BuiltinParameterGroup.%s" %IN[2])

TransactionManager.Instance.EnsureInTransaction(doc)

new_para = doc.FamilyManager.AddParameter(para_Name,param_Group,para_Type,False)

TransactionManager.Instance.TransactionTaskDone()

OUT = new_para