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

def decrypt(file, key, header_size = None):
	if header_size is None:
		header_size = 1024

	try:
		fencrypted = open(file, 'rb')
		
		content_encrypted = fencrypted.read()
		filesize = len(content_encrypted)
		keylen = len(key)

		recovered = ''
		full_recovered = ''
		
		if filesize <= header_size:
			for i in range(0,filesize):
				print filesize
				recovered = recovered + chr(ord(content_encrypted[i])^ord(key[i%keylen]))
			full_recovered = recovered
		else:
			for i in range(0,header_size):
				recovered = recovered + chr(ord(content_encrypted[i])^ord(key[i%keylen]))
			full_recovered = recovered + content_encrypted[header_size:]
		
		open(file[:-8], 'wb').write(full_recovered)
		fencrypted.close()
		print "[-]File %s recovered succesfully!\n" % file[:-8]
		return 0
	except:
		print "An error has occured!"
	
#main
print "\n*Nemucod File Recovery*\n"

if len(sys.argv) >= 3:
	os.chdir(sys.argv[1])
	if len(sys.argv) == 3:
		for file in glob.glob("*.crypted"):
			decrypt(file,sys.argv[2])
	else:
		for file in glob.glob("*.crypted"):
			decrypt(file,sys.argv[2],int(sys.argv[3]))
else:
	print "*ERROR: Incorrect number of arguments passed to the script!\n"
	print "Example: python NemucodFR.py folder key [header_size]\n"
	print "folder: a folder which contains encrypted files by Nemucod with .crypted extension;\n"
	print "key: the key recovered with the crack.py script."
