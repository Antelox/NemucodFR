"""

Nemucod Key Extractor

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org
Version: 0.36 - 06/22/2016

Released under MIT License

This script is able to recover files encrypted by the Nemucod Ransomware (the latest variants).

*NOTE*: This script doesn't handle the 7-Zip variant.

*NOTE*: You must use Python 2.7.* not 3+

For more information about the last Nemucod variants you can take a look at:

- https://glot.io/snippets/ee7hiif87k
- http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-11#entry4005316
- http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-12#entry4016916
- https://reaqta.com/2016/06/nemucod-meets-php/


DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Regardless, this script will only print the extracted key.
***NO FILE OPERATIONS WILL BE PERFORMED***

"""

import sys

print "\n*Nemucod Key Extractor*\n"

if len(sys.argv) == 3:
	fencrypted = open(sys.argv[1],'rb')
	fplain = open(sys.argv[2],'rb')

	content_encrypted = fencrypted.read()
	content_plain = fplain.read()
	
	if content_encrypted[0]=='7' and content_encrypted[1]=='z':
		print "*INFO*: A 7zip variant detected! Unfortunately this script can not handle it."
		sys.exit()
		
	if content_encrypted[1535] == content_plain[1535] and content_encrypted[2000] == content_plain[2000]:
		print "*INFO*: Encrypted header size = 1024 bytes\n" 
		print "*INFO*: Due to different Nemucod variants the key length can be as follows:\n"
		print "*INFO*: - 36 bytes\n"
		print "*INFO*: - 1024 bytes\n"
		print "*INFO*: - 102 bytes\n"
		print "*INFO*: Run this script again passing as an argument the key size.\n"
		print "*INFO*: For example - python NemucodKE.py encrypted original 102"
	else:
		print "*INFO*: Encrypted header size = 2048 bytes and key size = 255 bytes\n"
		key_size = 255
		
		key = ''
		
		for i in range(0,key_size):
			if i == key_size - 1:
				key = key + hex(ord(content_encrypted[i])^ord(content_plain[i]))
			else:
				key = key + hex(ord(content_encrypted[i])^ord(content_plain[i])) + ", "
	
		print "\n*KEY FOUND*: File \"key_2048_255.txt\" has been created."
		open("key_2048_255.txt", "wb").write("[" + key + "]")
	
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

	print "\n*KEY FOUND*: File \"key_1024_%s.txt\" has been created." % str(sys.argv[3])
	open("key_1024_" + str(sys.argv[3]) + ".txt", "wb").write("[" + key + "]")

	fencrypted.close()
	fplain.close()

else:
	print "*ERROR*: An incorrect number of arguments were passed to this script!\n"
	print "Example: python NemucodKE.py encrypted original\n"
	print "encrypted: A file encrypted by Nemucod with .crypted extension;\n"
	print "original: The same file as the .crypted file pulled from a backup or email for example."
