#How to use the Ironpython Libraries by adding it to the path
#http://www.ironpython.info/index.php?title=Using_the_Python_Standard_Library

import sys
sys.path.append(r"C:\Program Files (x86)\IronPython 2.7\Lib")
import json

#example to merge two with same keys
eng = IN[0]
ger = IN[1]

en_dicts = json.loads(eng)
de_dicts = json.loads(ger)

for key,value in en_dicts.items():
	new_value = de_dicts[key]
	new_name = new_value["Name"]
	en_dicts[key].update({"NewName": new_name})
	
data = json.dumps(en_dicts, ensure_ascii=False)
OUT = data
