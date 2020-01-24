#That’s because some modules are implemented using native 
#c# libs and reside in the IronPythonModules.dll, 
#which is loaded automatically at startup. 
#The rest of the ipy modules are implemented as python code 
#(and reside in the Lib folder) and are translated to the 
#CLR’s intermediate language every time you run the script:

import System
mods = None

for a in System.AppDomain.CurrentDomain.GetAssemblies():
	if 'IronPython.Modules' == a.GetName().Name:
		mods = a
		break

if mods is not None:
	OUT = [m.Key for m in mods.IronPython.Modules]
