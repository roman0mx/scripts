#!/opt/Python-2.7.14/bin/python

import pathlib
import subprocess

p = pathlib.Path(".")

BaseFormat = "sln16"
DestFormat = ["gsm","g729","ilbc","ulaw", "alaw", "g722"]

for i in range (0,len(DestFormat)):
	for child in p.rglob("*." + BaseFormat):
##	print child.absolute()
		myoptions = "file convert " + str(child.absolute()) + " " + str(child.absolute()).replace("."+BaseFormat,"."+DestFormat[i])
	        print "asterisk -rx "+ myoptions
		subprocess.call(["asterisk","-rx", myoptions])
	
# [x for x in p.iterdir() if x.is_dir()]

