"""

Nemucod Key Extractor

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org

Released under MIT License

This script is designed to work with the last variant of Nemucod Ransomware. For more informations you can take a look here:

https://glot.io/snippets/ee7hiif87k


DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Anyway this script print only the key extracted. No file operations will be performed.

"""

import sys

print "\n*Nemucod Key Extractor*\n"

if len(sys.argv)== 3:
	fencrypted = open(sys.argv[1],'rb')
	fplain = open(sys.argv[2],'rb')

	content_encrypted = fencrypted.read(36)
	content_plain = fplain.read(36)

	key = ''

	for i in range(0,36):
		key = key + chr(ord(content_encrypted[i])^ord(content_plain[i]))

	print "\n*KEY FOUND*: The key is: %s" % key

	fencrypted.close()
	fplain.close()
else:
	print "*ERROR: Incorrect number of arguments passed to the script!\n"
	print "Example: python NemucodKE.py encrypted original\n"
	print "encrypted: a file encrypted by Nemucod with .crypted extension;\n"
	print "original: the same file not encrypted of which you have a backup copy."