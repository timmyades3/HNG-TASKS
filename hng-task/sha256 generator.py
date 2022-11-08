import os
import hashlib


path = input(r'enter th path to the folder you want to generate sha256_hash for > ')
# input path directory example C:\Users\oluwa\Desktop\MY PROJECTS\HNG TASKS\hng-task\jsonfile_path
#N O T E :This is to generate sh256_hash for files in a folder, the files you want to generate sha256_hash for must be in a folder
folder_list=[]
#loop over files in path directory
file_count = 1
for file_n in os.listdir(path):
    sha256 = hashlib.sha256()
    with open(path + '\\' + str(file_n),"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256.update(byte_block)
            print('This is the SHA256 for file'+ ' '+str(file_count)+'  '+sha256.hexdigest() )
            file_count+= 1


#This is to generate sha256_hash for a single file 
import os
import hashlib

path = input(r'enter your file path > ')
# input a path example C:\Users\oluwa\Desktop\MY PROJECTS\HNG TASKS\hng-task\jsonfile_path\abdul-the-vibe.json
sha256 = hashlib.sha256()
with open( path,'rb') as opened_file:
  for block_byte in iter(lambda: opened_file.read(4069),b""):
    sha256.update(block_byte)
  print(sha256.hexdigest())  
 
