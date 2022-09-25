from fileinput import filename
import send2trash
import os
import shutil
from pathlib import Path

source= "/Documents/automate_the_boring_stuff"

for folder, subfolders, filenames in os.walk(source):
    for filename in filenames:
        filesize=int(os.path.getsize(folder+"/"+filename))/1024
        if filesize>10:
            print("File is: "+folder+"/"+filename+"/" +","+"\nSize is: "+str(filesize)+"kb")
            # send2trash.send2trash(filename)
        
