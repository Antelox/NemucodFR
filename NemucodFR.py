"""

Nemucod File Recovery

Coded by Antelox
Twitter: @Antelox
UIC R.E. Academy - quequero.org
Version: 0.36 - 06/22/2016

Released under MIT License

This script is able to recover files encrypted by the Nemucod Ransomware (the latest variants).

*NOTE*: This script doesn't handle the 7-Zip variant.

*NOTE*: You must use Python 2.7.* not 3+

*NOTE*: If you have problems with mapped drives you probably don't actually have that drive mapped under the elevated user.
		Try running with a UNC path instead.

For more information about the last Nemucod variants you can take a look at:

- https://glot.io/snippets/ee7hiif87k
- http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-11#entry4005316
- http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-12#entry4016916
- https://reaqta.com/2016/06/nemucod-meets-php/


DISCLAIMER
Use this script at your own risk. I'm not responsible for any data loss!
Regardless, this script doesn't overwrite and/or delete any files and creates new files with the decrypted data.
Please remove the .crypted files after you have verified the recovered files are correct either manually or using NemucodRE.py.

"""

import os
import sys
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
	print "*ERROR*: An incorrect number of arguments were passed to this script!\n"
	print "Example: python NemucodFR.py path key_file header_size\n"
	print "path: A path to a folder which contains files encrypted by Nemucod with .crypted extensions;\n"
	print "key_file: The file which contains the recovered key by NemucodKE.py script;\n"
	print "header_size: Size, from the beginning of the file, which was encrypted - info provided by NemucodKE.py script."
