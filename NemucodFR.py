"""

Nemucod File Recovery

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org
Version: 0.2 - 05/22/2016

Released under MIT License

This script is able to recover encrypted files by Nemucod Ransomware (the last 2 variants)

For more informations about this variant you can take a look at:

https://glot.io/snippets/ee7hiif87k

and here:

http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-11#entry4005316

DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Anyway the script doesn't overwrite and/or delete any files.

"""

import sys
import glob
import os

def decrypt(file, key, hsize):
	try:
		fencrypted = open(file, 'rb')
		
		content_encrypted = fencrypted.read()
		filesize = len(content_encrypted)
		
		recovered = ''
		full_recovered = ''
		
		if filesize <= hsize:
			for i in range(0,filesize):
				recovered = recovered + chr(ord(content_encrypted[i])^ord(key[i%len(key)]))
			full_recovered = recovered
		else:
			for i in range(0,hsize):
				recovered = recovered + chr(ord(content_encrypted[i])^ord(key[i%len(key)]))
			full_recovered = recovered + content_encrypted[hsize:]
		
		open(file[:-8], 'wb').write(full_recovered)
		fencrypted.close()
		print "[+]File %s recovered succesfully!\n" % file[:-8]
		return 0
	except:
		print "An error has occured!"
	
#main
print "\n*Nemucod File Recovery*\n"

if len(sys.argv) == 4:
	os.chdir(sys.argv[1])
	for file in glob.glob("*.crypted"):
		decrypt(file,sys.argv[2],int(sys.argv[3]))
else:
	print "*ERROR: Incorrect number of arguments passed to the script!\n"
	print "Example: python NemucodFR.py folder key header_size key_size\n"
	print "folder: a folder which contains encrypted files by Nemucod with .crypted extension;\n"
	print "key: the key recovered with the NemucodKE.py script;\n"
	print "header_size: size, from beginning of the file, which it was encrypted - provided by NemucodKE.py script."