#!/usr/bin/python

import os
import subprocess



def fac(a)
	if a == 1:
		return 1
	else:
		return a * fac(a-1)

		


## Incluir la '/' al final del Path definido
myPath="/opt/convert/"
OrigFileExt = ".sln16"
DestFileExt = ".g729"
i=0

myFileList = os.listdir(myPath)

for i in range (0, len(myFileList)):
#        print myPath
#        print i

        if os.path.isfile(myFileList[i]):
#               print myFileList[i]
                fn, fxt = os.path.splitext(myFileList[i])
#                print fn
#                print fxt

                if (fxt == OrigFileExt):
                        subprocess.call(["asterisk", "-rx", "file convert " + myPath + myFileList[i] + " " + myPath + fn + DestFileExt])

## Fin




