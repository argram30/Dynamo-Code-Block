def tolist(obj1):
	if hasattr(obj1,"__iter__"): return obj1
	else: return [obj1]