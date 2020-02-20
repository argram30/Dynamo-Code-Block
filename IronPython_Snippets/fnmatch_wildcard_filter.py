import sys
sys.path.append(r"C:\Program Files (x86)\IronPython 2.7\Lib")
import fnmatch

data = IN[0]

OUT = fnmatch.filter(data, '???_*')
