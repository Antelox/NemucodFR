"""

Nemucod Remove Encrypted

Coded by Alex
Twitter: @AlexJamesHaines
Freedom I.T. Systems LTD - freedomitsolutions.co.uk
Version: 0.36 - 06/22/2016

Released under MIT License

This script helps remove the left over .crypted files once you are happy they have been recovered.

*NOTE*: You must use Python 2.7.* not 3+

*NOTE*: If you have problems with mapped drives you probably don't actually have that drive mapped under the elevated user.
		Try running with a UNC path instead.

REFERENCES
http://code.activestate.com/recipes/577058 for the user query code.

DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!

"""

import os
import sys
import ast

def delete(file):
	try:
		os.remove(file)
		print "[-] File \"%s\" deleted succesfully!\n" % file[:-8]
		return 0
	except:
		print "An error has occured!"
		
def query_yes_no(question, default="no"):
    valid = {"yes":"yes",   "y":"yes",  "ye":"yes",
             "no":"no",     "n":"no"}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default answer: '%s'" % default)

    while 1:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

#Main
print "\n*Nemucod Remove Encrypted*\n"

answer = query_yes_no("Are you sure that you want to continue to remove all .crypted files from your system?")
if answer == "no" :
	print "\nOK - Quitting now...\n"
	sys.exit()

if len(sys.argv) == 2:
	for subdir, dirs, files in os.walk(str(sys.argv[1])):
		for file in files:
			if file.endswith('.crypted'):
				full_path = os.path.join(subdir, file)
				delete(full_path)
else:
	print "*ERROR*: An incorrect number of arguments were passed to this script!\n"
	print "Example: python NemucodRE.py path\n"
	print "path: A path to a folder which contains files encrypted by Nemucod with .crypted extensions;\n"
