"""

Nemucod Path Tester

Coded by Alex
Twitter: @AlexJamesHaines
Freedom I.T. Systems LTD - freedomitsolutions.co.uk
Version: 0.36 - 06/22/2016

Released under MIT License

This script helps troubleshoot errors with paths that may break the execution of the other scripts.

*NOTE*: You must use Python 2.7.* not 3+

*NOTE*: If you have problems with mapped drives you probably don't actually have that drive mapped under the elevated user.
		Try running with a UNC path instead.


DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Regardless, this script doesn't overwrite and/or delete any files.

"""

import os
import sys

print "\n*Nemucod Path Tester*\n"

if len(sys.argv) == 2:

	path = sys.argv[1]
	dir, filen = os.path.split(path)

	print "Directory:", dir
	if os.path.exists(dir):
		print "Directory found - yay :)\n"
	else:
		print "Directory can not be found - boo :(\n"
		sys.exit()

	if not filen:
		print "No filename provided!!!"
		sys.exit()

	print "Filename:", filen
	if os.path.exists(path):
		print "Filename found - yay :)\n"
	else:
		print "Filename can not be found - boo :(\n"
		print "Directory Contents:"
		for fn in os.listdir(dir):
			print fn

else:
	print "*ERROR*: An incorrect number of arguments were passed to this script!\n"
	print "Example: python NemucodPT.py path\n"
	print "path: A path to a folder which contains the target file.\n"
