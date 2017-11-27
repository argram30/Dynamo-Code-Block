def toName(_list):
	
	if checkList(_list):
		names = ' x '.join(str(name) for name in _list)
		return names
	else:
		return _list
