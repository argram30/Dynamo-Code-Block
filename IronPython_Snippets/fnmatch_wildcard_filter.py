import sys
sys.path.append(r"C:\Program Files (x86)\IronPython 2.7\Lib")
import fnmatch

data = IN[0]
output = []

OUT = fnmatch.filter(data, 'gg_???_TU_*')
