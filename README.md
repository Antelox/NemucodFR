# NemucodFR
Extract the key and use it to recover files that have been excrypted by Nemucod Ransomware

- **NemucodKE.py** - the python script to extract the key (*KE* means Key Extractor);
- **NemucodFR.py** - the python script to recover the encrypted file (*FR* means File Recovery);
- **NemucodPT.py** - the python script to test paths in case of errors (*PT* means Path Tester);
- **NemucodRE.py** - the python script to remove the encrypted file (*RE* means Remove Encrypted).

*NOTE*: You must use Python 2.7.* not 3+

# Changelog

FIRST COMMIT: 05/01/2016 - ver. 0.1

In the last variant of **Nemucod Ransomware**, discovered by *ReaQta's R&D Team* [1], the file is encrypted through a custom xorer that XORs the first *1024* bytes of each targeted file with a *36* bytes long randomly generated key. In the previous two Nemucod variants, you could see first a xor operation like the one found in this variant but with an hardcoded key (so not randomly generated) inside the executabled downloaded by the Javascript code [2]. Then Nemucod has replaced the xor encryption process with 7zip CLI version [3]. Now it's come back with the xor encryption approach.

UPDATE: 05/22/2016 - ver. 0.2

Found in the wild by [@demonslay335](https://twitter.com/demonslay335) a new Nemucod variant which encrypts first 2048 bytes with a key of 255 bytes. The script handles also this one.

UPDATE: 06/11/2016 - ver. 0.3

2 new Nemucod variants discovered: this time the header size is 1024 bytes but key length changes and can be: 1024 bytes [4] or 102 bytes [5]. The script now handles also these ones.

UPDATE: 06/15/2016 - ver. 0.35

NemucodKE.py saves the text file which contains the key with different names based on the header/key length.
NemucodFR.py searches recursively files and folders from the path passed as argument (open the command prompt as Administrator).

UPDATE: 06/22/2016 - ver. 0.36

NemucodPT.py helps troubleshoot errors with paths that may break the execution of the other scripts.
NemucodRE.py searches recursively files and folders from the path passed as argument (open the command prompt as Administrator).
Language tweaks all round.

# References

[1] https://glot.io/snippets/ee7hiif87k

[2] https://blog.fortinet.com/post/nemucod-adds-ransomware-routine

[3] https://reaqta.com/2016/04/nemucod-meets-7zip-to-launch-ransomware

[4] http://www.bleepingcomputer.com/forums/t/608045/crypted-ransomware-nemucod-decrypttxt-support-and-help-topic/page-12#entry4016916

[5] https://reaqta.com/2016/06/nemucod-meets-php/

# How to use these scripts
These scripts are able to extract the key first, and recover whole encrypted data then ONLY AND ONLY IF you have one *exact* backup copy of the file that was encrypted.

_Example scenario_

A friend, a girlfriend or any others sent you an email with *documents.zip* file in attachment. You download this file on your computer and extract the whole content to work on. After a couple of hours/days you get, unfortunately, infected by Nemucod Ransomware and your *documents.zip* file (as well as others files) was encrypted and renamed *documents.zip.crypted*. At this point you can use the **NemucodKE.py** python script to extract the key in this manner:

Open a command prompt as Administrator. If you don't know how to do it see [here](https://technet.microsoft.com/en-us/library/cc947813(v=ws.10).aspx)

Move inside the NemucodFR folder cloned from this repository and do:

*python NemucodKE.py documents.zip.crypted documents.zip*

Obviously you have the original *documents.zip* file copy inside the email server!

As a result of the script, based on the Nemucod variant, you will get:

1) If the Nemucod variant is the one with header size of 2048 bytes and the key size of 255 bytes, the _key\_2048\_255.txt_ file which you can pass it as command line argument to the NemucodFR.py script (see below);

2) If the Nemucod variant is the one with header size of 1024 bytes then could be 3 different key sizes:
- 36 bytes;
- 1024 bytes;
- 102 bytes.

So you have to make 3 attempts, one for each key size.
For example you can try:

*python NemucodKE.py encrypted original 102*

at this point you get the _key\_1024\_102.txt_ file and you can use it together with NemucodFR.py script (see below). If the file recovered with this key size is not equal to the orginal one then repeat the same operation but with a different key size.


After that you got the right key text file, you can use the **NemucodFR.py** script in this manner:

*python NemucodFR.py path key_file header_size*

where:

- *path* is the path to a folder which contains the .crypted files encrypted and renamed by Nemucod Ransomware. The script, starting from the path passed as argument, will iterate recursively files and sub-directories to search for .crypted files, so make sure that the key is the right one before to run this script, for example, from the C:\\ (more info [here](https://github.com/Antelox/NemucodFR#how-to-know-if-the-script-has-extracted-the-right-key)). If you want to make a try about the paths (mapped drives on your network, etc.), before that you run this script, you can use the **NemucodPT.py** script in this manner:

	*python NemucodPT.py path_to_test*

- *key_file* the file which contains the recovered key by NemucodKE.py script. It can be the following ones:
	
  _key\_1024\_36.txt_

	_key\_1024\_102.txt_
	
	_key\_1024\_1024.txt_
	
	_key\_2048\_255.txt_
	
- *header_size* is the size, from beginning of the file, which it was encrypted - provided by NemucodKE.py script. It can bethe following ones:

	_1024_
	
	_2048_

As results we will get the decrypted files (I hope) :D

If it's all ok and you want to delete .crypted files from your drives, you can use **NemucodRE.py** script in this manner:

*python NemucodRE.py "C:\"*

with this command you will delete whole .crypted files on drive C.

*NOTE*: Execute this command ONLY after that you have recovered the files!!!

Of course this is only an example. Any files of which you have a backup copy on external device and/or in a cloud storage service will be fine, the important is that it's the same one that was encrypted.

# How to know if the script has extracted the right key
It's really simple. Before you start to decrypt your data, you can create a "*test*" folder in which you can copy an encrypted file. Make your try with the file inside "*test*" folder and if you will see your original file, so it's the right key. Of course if you make a try and the file is not recovered then, before that you start to make another try, delete first the file inside "*test*" folder and copy again the encrypted file inside it.

# Note
I thought this script as an additional possibility that a Nemucod's victim can have in addition to other already known solutions.

# Disclaimer
*Use these scripts at your own risk. I'm not responsible for any data loss!
Regardless, the main scripts don't overwrite and/or delete any files and create new files with the decrypted data.
Only the NemucodRE.py script removes data from your devices.*

# License
See the LICENSE file for license rights and limitations (*MIT*).
