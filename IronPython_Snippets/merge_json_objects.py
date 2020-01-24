import sys
sys.path.append(r"C:\Program Files (x86)\IronPython 2.7\Lib")
import json

#JsonData package
import clr
clr.AddReference("JsonData")
from JsonData.Utilities import Parse

eng = IN[0]
ger = IN[1]

en_dicts = json.loads(eng)
de_dicts = json.loads(ger)

for key,value in en_dicts.items():
	new_value = de_dicts[key]
	new_name = new_value["Name"]
	en_dicts[key].update({"DeutschName": new_name})
	
data = json.dumps(en_dicts, ensure_ascii=False)
OUT = Parse.String(data)
