"""

Nemucod File Recovery

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org
Version: 0.35 - 06/15/2016

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
Anyway the script doesn't overwrite and/or delete any files.

"""

import sys
import os
import ast

def decrypt(file, key, hsize):
	try:
		fencrypted = open(file, 'rb')
		fkey = open(key,"rb")
		key1 = ast.literal_eval(fkey.read())
		content_encrypted = fencrypted.read()
		filesize = len(content_encrypted)
		
		recovered = ''
		full_recovered = ''
		
		if filesize <= hsize:
			for i in range(0,filesize):
				recovered = recovered + chr(ord(content_encrypted[i])^key1[i%len(key1)])
			full_recovered = recovered
		else:
			for i in range(0,hsize):
				recovered = recovered + chr(ord(content_encrypted[i])^key1[i%len(key1)])
			full_recovered = recovered + content_encrypted[hsize:]
		
		open(file[:-8], 'wb').write(full_recovered)
		fencrypted.close()
		print "[+] File \"%s\" recovered succesfully!\n" % file[:-8]
		return 0
	except:
		print "An error has occured!"
	
#main
print "\n*Nemucod File Recovery*\n"

if len(sys.argv) == 4:
	for subdir, dirs, files in os.walk(str(sys.argv[1])):
		for file in files:
			if file.endswith('.crypted'):
				full_path = os.path.join(subdir, file)
				decrypt(full_path, sys.argv[2], int(sys.argv[3]))
else:
	print "*ERROR: Incorrect number of arguments passed to the script!\n"
	print "Example: python NemucodFR.py path key_file header_size\n"
	print "path: a path t a folder which contains encrypted files by Nemucod with .crypted extension;\n"
	print "key_file: the file which contains the recovered key by NemucodKE.py script;\n"
	print "header_size: size, from beginning of the file, which it was encrypted - info provided by NemucodKE.py script."
