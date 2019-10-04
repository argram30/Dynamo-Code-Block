import clr

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import FilteredElementCollector

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def tolist(obj1):
	if hasattr(obj1,"__iter__"): return obj1
	else: return [obj1]

cat = UnwrapElement(IN[0])
OUT = []

ueWrapper = None
wrappers = clr.GetClrType(Revit.Elements.ElementWrapper).GetMethods()
for w in wrappers:
	if w.ToString().startswith("Revit.Elements.UnknownElement"):
		ueWrapper = w
		break

if ueWrapper is not None:
	fec = FilteredElementCollector(doc).WhereElementIsNotElementType()
	if cat is not None:
		fec = fec.OfCategoryId(cat.Id)
	view_el = []
	for e in fec:
		view_el.append(ueWrapper.Invoke(None, (e, True) ) )
	OUT.append(view_el)