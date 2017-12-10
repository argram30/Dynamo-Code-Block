#Copyright 2017. All rights reserved. Bimorph Consultancy LTD, 5 St Johns Lane, London EC1M 4BH www.bimorph.co.uk
#Written by Thomas Mahon @Thomas__Mahon info@bimorph.co.uk Package: bimorphNodes
#GitHub: https://github.com/ThomasMahon/bimorphNodes/
#Follow: facebook.com/bimorphBIM | linkedin.com/company/bimorph-bim | @bimorphBIM

import clr
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import TextBox
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import TaskDialogCommonButtons

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import *

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

def convertToList(testList):
	if isinstance(testList, list):
		return testList
	else:
		return [testList]
				
def convertToListOfLists(testColourList, messsageTitle):
	msgMessage = "bimorph.CreateNewLineStyles:\nColour data structure error - The input Line Style colours are not in sublists. Each RGB colour set should be defined in a sublist, eg: { {red, green, blue} }"
	if isinstance(testColourList, list): 
		if isinstance(testColourList[0], list):
			
			for i in testColourList: 
				if isinstance(i, list) and len(i) == 3:
					continue
				else: 
					TaskDialog.Show(messsageTitle, msgMessage, TaskDialogCommonButtons.Ok)
					testColourList = True
					return testColourList
					
			return testColourList 
				
		else:
			if len(testColourList) == 3: 
				return [testColourList]
			else: 
				TaskDialog.Show(messsageTitle, msgMessage, TaskDialogCommonButtons.Ok)
				testColourList = True
				return testColourList
	else:
		TaskDialog.Show(messsageTitle, msgMessage, TaskDialogCommonButtons.Ok)
		testColourList = True
		return testColourList


messsageTitle = "bimorph.CreateNewLineStyles"

run = IN[3]

if run:
	lineStylesName =  convertToList( IN[0] )
	lineStylesWeight =  convertToList( IN[1] )
	lineStylesColour = convertToListOfLists( IN[2], messsageTitle )
	if lineStylesColour == True:
		OUT = "Colour data structure error - colours should be input as integer sublists defining the RGB values", []
	else:
		listLacingCheck = False 
		if len(lineStylesName) == len(lineStylesWeight) == len(lineStylesColour):
			listLacingCheck = True
		else:
			TaskDialog.Show(messsageTitle, "bimorph.CreateNewLineStyles:\nLacing error - The number of items in the name, line weight and line colours input lists do not match. Ensure there are an equal number of items in each list and try again", TaskDialogCommonButtons.Ok)
			OUT = "Lacing error - Data mismatch; ensure an equal number of items are in each input", []
		
		if listLacingCheck:
			TransactionManager.Instance.EnsureInTransaction(doc)
			doc.Regenerate()
			
			categories = doc.Settings.Categories
			lineCategory =  doc.Settings.Categories.get_Item( BuiltInCategory.OST_Lines )
			lineSubCategory = lineCategory.SubCategories
			
			newLineStyleList = zip(lineStylesName, lineStylesWeight, lineStylesColour)
			
			newLineStyleOUT = []
			errorReport = []
			for lineStyleData in newLineStyleList:
				try:
					inProject = False
					name = lineStyleData[0]
					for i in lineSubCategory:
						if i.Name == name:
							inProject = True
							errorReport.Add( "LineStyle " + name + " exists in the current document and cannot be created")
							break
					if inProject:
						continue
					else:
						newLineStyle = categories.NewSubcategory(lineCategory, name);
						newLineStyle.LineColor = Color(lineStyleData[2][0], lineStyleData[2][1], lineStyleData[2][2]);
						newLineStyle.SetLineWeight(lineStyleData[1], GraphicsStyleType.Projection);
						
						newLineStyleOUT.Add( newLineStyle.GetGraphicsStyle(GraphicsStyleType.Projection) )
					
				except:
					errorReport.Add( "LineStyle creation failed Check your data types are correctly wired to the node and retry" )
			
			TransactionManager.Instance.TransactionTaskDone()
			
			if errorReport == []:
				OUT = "All LineStyles successfully created", newLineStyleOUT
			else:
				OUT = errorReport, newLineStyleOUT
