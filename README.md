# NemucodFR
Extract the key and use it to recover encrypted files by Nemucod Ransomware

- **NemucodKE.py** - the python script to extract the key (*KE* means Key Extractor);
- **NemucodFR.py** - the python script to recover the encrypted file (*FR* means File Recovery).

In the last variant of **Nemucod Ransomware**, discovered by *ReaQta's R&D Team* [1], the file is encrypted through a custom xorer that XORs the first *1024* bytes of each targeted file with a *36* bytes long randomly generated key. In the previous two Nemucod variants, you could see first a xor operation like the one found in this variant but with an hardcoded key (so not randomly generated) inside the executabled downloaded by the Javascript code [2]. Then Nemucod has replaced the xor encryption process with 7zip CLI version [3]. Now it's come back with the xor encryption approach.

UPDATE: 05/22/2016

Found in the wild by [@demonslay335](https://twitter.com/demonslay335) a new Nemucod variant which encrypts first 2048 bytes with a key of 255 bytes. The script handles also this one.

[1] https://glot.io/snippets/ee7hiif87k

[2] https://blog.fortinet.com/post/nemucod-adds-ransomware-routine

[3] https://reaqta.com/2016/04/nemucod-meets-7zip-to-launch-ransomware

# How to use these scripts
These scripts are able to extract the key first, and recover whole encrypted data then ONLY AND ONLY IF you have one *exact* backup copy of the file that was encrypted.

_Example scenario_

A friend, a girlfriend or any others sent you an email with *documents.zip* file in attachment. You download this file on your computer and extract the whole content to work on. After a couple of hours/days you get, unfortunately, infected by Nemucod Ransomware and your *documents.zip* file (as well as others files) was encrypted and renamed *documents.zip.crypted*. At this point you can use the **NemucodKE.py** python script to extract the key in this manner:

*python NemucodKE.py documents.zip.crypted documents.zip*

Obviously you have the original *documents.zip* file copy inside the email server!

As a result of the script you will get the key.

After that you got the key, you can use the **NemucodFR.py** script in this manner:

*python NemucodFR.py folder key header_size key_size*

where:

- *folder* is the folder which contains the .crypted files encrypted and renamed by Nemucod Ransomware;
- *key* is the key extracted with the previous step;
- *header_size* is the size, from beginning of the file, which it was encrypted - provided by NemucodKE.py script;
- *key_size* is the size of the key - provided by NemucodKE.py script.

As results we will get the decrypted files (I hope) :D

Of course this is only an example. Any file of which you have a backup copy on external device and/or in a cloud storage service will be fine, the important is that it's the same one that was encrypted.

# How to know if the script has extracted the right key
It's really simple. Before you start to decrypt your data, you can create a "*test*" folder in which you can copy an encrypted file. Make your try with the file inside "*test*" folder and if you will see your original file, so it's the right key. Of course if you make a try and the file is not recovered then, before that you start to make another try, delete first the file inside "*test*" folder and copy again the encrypted file inside it.

# Note
I thought this script as an additional possibility that a Nemucod's victim can have in addition to other already known solutions.

# Disclaimer
*Use these scripts at your own risk. I'm not responsible for any data loss!
Anyway the scripts don't overwrite and/or delete any files.*

# License
See the LICENSE file for license rights and limitations (*MIT*).
