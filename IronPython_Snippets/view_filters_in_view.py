import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])
filters = UnwrapElement(IN[1])
boollist = []

for filter in filters:
	thisfilter = False
	for view in views:
		if view != None:
			check = view.IsFilterApplied(filter.Id)
			if check:
				thisfilter = True
				break
			else: 
				pass
	boollist.append(thisfilter)
	
OUT = boollist