#gets the parameter value of the element
def getValue(element, param_name):
	if checkList(param_name):
		multi = []
		for name in param_name:
			multi.append(element.GetParameterValueByName(name))
		return multi
		
	else: 
		return element.GetParameterValueByName(param_name)
		
