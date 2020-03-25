# -*- coding: utf-8 -*-

data = IN[0]
pattern = ""
wand_texts = ["wand","wa","wall"]
boden_texts = ["boden","bo","decken","de","floor","fl","ceiling","ce"]
rund_texts = ["rund","ru","round","ro"]
recht_texts = ["rechteck","re","rectangle"]
splitted = [i.lower().strip() for i in data.split(",")]

#inserts string at a position in string
def insert_str(orig, pos, toinsert):
    orig = orig[:pos] + toinsert + orig[pos:] 
    return orig

#Regex Pattern doesnot contain
contains_not = r"(?!.*sonderdurchführung)"
schlitz = r"|.*schlitz|.*ws"
rund = r"|.*rund|.*rh"
recht = r"|.*rechteck|.*re"

#Regex Pattern contains
wand = r"wanddurchbruch|wd_|wa_"
boden = r"(boden|decken)durchbruch|dd_"

#disperse
if len(splitted) == 2:
	if splitted[0] in wand_texts and splitted[1] in rund_texts:
		pattern = insert_str(contains_not, -1, schlitz+rund) + wand
	elif splitted[0] in wand_texts and splitted[1] in recht_texts:
		pattern = insert_str(contains_not, -1, schlitz+recht) + wand
	elif splitted[0] in boden_texts and splitted[1] in rund_texts:
		pattern = insert_str(contains_not, -1, schlitz+recht) + boden
	elif splitted[0] in boden_texts and splitted[1] in recht_texts:
		pattern = insert_str(contains_not, -1, schlitz+recht) + boden
	else:
		pattern
else:
	pattern
		
OUT = pattern
