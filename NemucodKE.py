"""

Nemucod Key Extractor

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org
Version: 0.3 - 06/11/2016

Released under MIT License

This script is able to recover encrypted files by Nemucod Ransomware (the last variants)
NOTE: This script doesn't handle 7-Zip variant

For more information about the last Nemucod variants you can take a look at:

- https://glot.io/snippets/ee7hiif87k
- http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-11#entry4005316
- http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-12#entry4016916
- https://reaqta.com/2016/06/nemucod-meets-php/


DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Anyway this script print only the key extracted. No file operations will be performed.

"""

import sys

print "\n*Nemucod Key Extractor*\n"

if len(sys.argv) == 3:
	fencrypted = open(sys.argv[1],'rb')
	fplain = open(sys.argv[2],'rb')

	content_encrypted = fencrypted.read()
	content_plain = fplain.read()
	
	if content_encrypted[0]=='7' and content_encrypted[1]=='z':
		print "*INFO*: 7zip variant detected! This script can not handle it."
		sys.exit()
		
	if content_encrypted[1535] == content_plain[1535] and content_encrypted[2000] == content_plain[2000]:
		print "*INFO*: encrypted header size = 1024 bytes\n" 
		print "*INFO*: due to different Nemucod variants key length can be as follow:\n"
		print "*INFO*: - 36 bytes\n"
		print "*INFO*: - 1024 bytes\n"
		print "*INFO*: - 102 bytes\n"
		print "*INFO*: Run again this script passing as argument the key size.\n"
		print "*INFO*: For example - python NemucodKE.py encrypted original 102"
	else:
		print "*INFO*: encrypted header size = 2048 bytes and key size = 255 bytes\n"
		key_size = 255
		
		key = ''
		
		for i in range(0,key_size):
			if i == key_size - 1:
				key = key + hex(ord(content_encrypted[i])^ord(content_plain[i]))
			else:
				key = key + hex(ord(content_encrypted[i])^ord(content_plain[i])) + ", "
	
		print "\n*KEY FOUND*: key.txt file created."
		open("key.txt", "wb").write("[" + key + "]")
	
		fencrypted.close()
		fplain.close()
		sys.exit()
	
elif len(sys.argv) == 4:
	fencrypted = open(sys.argv[1],'rb')
	fplain = open(sys.argv[2],'rb')

	content_encrypted = fencrypted.read()
	content_plain = fplain.read()
	
	key = ''
	key_size = int(sys.argv[3])
	for i in range(0,key_size):
		if i == key_size-1:
			key = key + hex(ord(content_encrypted[i])^ord(content_plain[i]))
		else:
			key = key + hex(ord(content_encrypted[i])^ord(content_plain[i])) + ", "

	print "\n*KEY FOUND*: key.txt file created."
	open("key.txt", "wb").write("[" + key + "]")

	fencrypted.close()
	fplain.close()

else:
	print "*ERROR: Incorrect number of arguments passed to the script!\n"
	print "Example: python NemucodKE.py encrypted original\n"
	print "encrypted: a file encrypted by Nemucod with .crypted extension;\n"
	print "original: the same file not encrypted of which you have a backup copy."
