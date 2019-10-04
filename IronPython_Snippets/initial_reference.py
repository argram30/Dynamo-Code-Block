import clr

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk

clr.AddReference("RevitNodes")
import Revit

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import geometry conversion extension methods
clr.ImportExtensions(Revit.GeometryConversion)

# Import Element wrapper extension methods
clr.ImportExtensions(Revit.Elements)

#https://github.com/DynamoDS/Dynamo/wiki/Python-0.6.3-to-0.7.x-Migration