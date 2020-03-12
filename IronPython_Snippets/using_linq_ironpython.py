import clr
clr.AddReference("System.Core")
import System
clr.ImportExtensions(System.Linq)

# https://daren-thomas.gitbooks.io/scripting-autodesk-revit-with-revitpythonshell/content/using_linq_in_ironpython/
# will print 3 and 4
[2, 3, 4].Where(lambda x: x != 2).ToList().ForEach(System.Console.WriteLine)
