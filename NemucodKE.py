"""

Nemucod Key Extractor

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org
Version: 0.2 - 05/22/2016

Released under MIT License

This script is designed to work with the 2 last variants of Nemucod Ransomware.

For more informations you can take a look here:

https://glot.io/snippets/ee7hiif87k

and here: 

http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-11#entry4005316

DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Anyway this script print only the key extracted. No file operations will be performed.

"""

import sys

print "\n*Nemucod Key Extractor*\n"

if len(sys.argv)== 3:
	fencrypted = open(sys.argv[1],'rb')
	fplain = open(sys.argv[2],'rb')

	content_encrypted = fencrypted.read()
	content_plain = fplain.read()
	
	if content_encrypted[0]=='7' and content_encrypted[1]=='z':
		print "*INFO*: 7zip variant detected! This script can not handle it."
		sys.exit()
		
	if content_encrypted[1535] == content_plain[1535] and content_encrypted[2000] == content_plain[2000]:
		print "*INFO*: encrypted header size = 1024 bytes and key size = 36 bytes\n"
		print "*INFO*: pass these 2 numbers as argument to NemucodFR.py script.\n"
		key_size = 36
	else:
		print "*INFO*: encrypted header size = 2048 bytes and key size = 255 bytes\n"
		print "*INFO*: pass these 2 numbers as argument to NemucodFR.py script.\n"
		key_size = 255
	
	key = ''

	for i in range(0,key_size):
		key = key + chr(ord(content_encrypted[i])^ord(content_plain[i]))

	print "\n*KEY FOUND*: The key is: %s" % key

	fencrypted.close()
	fplain.close()
else:
	print "*ERROR: Incorrect number of arguments passed to the script!\n"
	print "Example: python NemucodKE.py encrypted original\n"
	print "encrypted: a file encrypted by Nemucod with .crypted extension;\n"
	print "original: the same file not encrypted of which you have a backup copy."