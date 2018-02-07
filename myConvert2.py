#!/usr/bin/python

import os
import subprocess
import sys


def fac(a):
	if a == 1:
		return 1
	else:
		return a * fac(a-1)




## Incluir la '/' al final del Path definido

def myAudioConvert(myPath=os.path.abspath(os.path.curdir), OrigFileExt=".sln16", DestFileExt=".g729", IsRecur="R"):

os.path.abspath(os.path.curdir)
	if myPath == "":
		myPath = os.getcwd() + "/"
	else:
		if myPath[-1] != "/":
			myPath = myPath + "/"


	if OrigFileExt == "":
		OrigFileExt = ".sln16"
	else:
		if OrigFileExt[0] != ".":
			OrigFileExt = "." + OrigFileExt


	if DestFileExt == "":
		DestFileExt = ".g729"
	else:
		if DestFileExt[0] != ".":
			DestFileExt = "." + DestFileExt
	

	if IsRecur == "":
		r = 0
	else:
		if IsRecur == "r" or IsRecur == "R":
			r=1
		else:
			r=0
	
	
	i=0
	
##	print "%s %s %s %s r es igual a %d" % (myPath, OrigFileExt, DestFileExt, IsRecur, r)
	
	myFileList = os.listdir(myPath)

	for i in range (0, len(myFileList)):
#		print myPath
#		print i

		if os.path.isfile(myFileList[i]):
#		   	print myFileList[i]
		        fn, fxt = os.path.splitext(myFileList[i])
#		        print fn
			print "%s  %s" % (fxt, OrigFileExt)
			if (fxt == OrigFileExt):
		            	subprocess.call(["asterisk", "-rx", "file convert " + myPath + myFileList[i] + " " + myPath + fn + DestFileExt])

	    
		if (os.path.isdir(myFileList[i]) and r == 1):
			print "%s  %s  %s %s %s" % (myPath, myFileList[i], OrigFileExt, DestFileExt, IsRecur)
	    		myAudioConvert(myPath + myFileList[i], OrigFileExt, DestFileExt, IsRecur)


## Main Prog

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

#for i in range (0, count):
#	print sys.argv[i]
	
if count+1 == 1:
##	print 'La forma de usar el programa es la siguiente:\\n %(program_name)s arg1 arg2 arg3' % {'program_name'}
##	print """\n La forma de usar el programa es la siguiente:
##	
##	%s Path ExtensionOrigen ExtensionDestino Recursion?
##	
##	Ejemplo:
##	
##	%s /opt/convert  slin  gsm R """ % (program_name, program_name)
##
	 myAudioConvert()
	 
elif count+1 == 2:
	myAudioConvert(arguments[0])

elif count+1 == 3:
	myAudioConvert(arguments[0], arguments[1])

elif count+1 == 4:
	myAudioConvert(arguments[0], arguments[1], arguments[2])

elif count+1 == 5:
	myAudioConvert(arguments[0], arguments[1], arguments[2], argunments[3])

elif count > 6:
	print """
	
	Demasiados Argumentos,
	
        La forma de usar el programa es la siguiente:
	        
        %s Path ExtensionOrigen ExtensionDestino Recursion?
	           
	Ejemplo:
	                        
	%s /opt/convert  slin  gsm R
	""" % (program_name, program_name)
                                  
else:
	
	print "Esto salio mal"
	
## Fin

