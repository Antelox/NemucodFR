"""

Nemucod File Recovery

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org

Released under MIT License

This script is able to recover encrypted files by Nemucod Ransomware (last variant)

For more informations about this variant you can take a look at:

https://glot.io/snippets/ee7hiif87k

DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Anyway the script doesn't overwrite and/or delete any files.

"""

import sys
import glob
import os

def decrypt(file, key):
	try:
		fencrypted = open(file, 'rb')
		
		content_encrypted = fencrypted.read()
		filesize = len(content_encrypted)
		
		recovered = ''
		full_recovered = ''
		
		if filesize <= 1024:
			for i in range(0,filesize):
				recovered = recovered + chr(ord(content_encrypted[i])^ord(key[i%36]))
			full_recovered = recovered
		else:
			for i in range(0,1024):
				recovered = recovered + chr(ord(content_encrypted[i])^ord(key[i%36]))
			full_recovered = recovered + content_encrypted[1024:]
		
		open(file[:-8], 'wb').write(full_recovered)
		fencrypted.close()
		print "[-]File %s recovered succesfully!\n" % file[:-8]
		return 0
	except:
		print "An error has occured!"
	
#main
print "\n*Nemucod File Recovery*\n"

if len(sys.argv) == 3:
	os.chdir(sys.argv[1])
	for file in glob.glob("*.crypted"):
		decrypt(file,sys.argv[2])
else:
	print "*ERROR: Incorrect number of arguments passed to the script!\n"
	print "Example: python NemucodFR.py folder key\n"
	print "folder: a folder which contains encrypted files by Nemucod with .crypted extension;\n"
	print "key: the key recovered with the crack.py script."