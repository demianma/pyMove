import shutil
import os
import re

# Set source, destination and list file.
_Source = ''
_Destination = 'destination_folder'
_List = 'exemple_list.txt'

#main
dir = os.path.dirname(__file__)
src = os.path.join(dir, _Source)
dst = os.path.join(dir, _Destination)
names = os.path.join(dir, _List)

with open(names, 'r') as fread:
    for line in fread:
        src_file_path = src + line.rstrip('\n')
        shutil.move(src_file_path,dst)
        #print 'Movido ' + src_file_path
