# This tool is used for delete any data that exists from deleted files.
# Deleted files remain on desk even if it was deleted
# so to delete these data permenantly, we have to write on it again.
# This tool creates a new file and fill it with null byte 0x00
# and the file's size is the whole free space on the volume.

import random
import string
import sys, os
import shutil


Path = sys.argv[1]
Path = Path[0:-1] + "\\" if Path[-1] == "\"" else Path

# First check if the path is directory or mount point and exists
if (os.path.isdir(Path) or os.path.ismount(Path)) and os.path.exists(Path):

    #Create a random 200 alphanumeric characters
    #so we could sure that this filenaame will not be exists
    FileName = ''.join(random.choices(string.ascii_letters +  string.digits, k=200))
    Path = Path + FileName + ".txt"
    
    FreeBytes = shutil.disk_usage(Path.split("\\", 1)[0]).free

    print("Please Don\'t use this disk while the tool is running")
    with open(Path, "wb") as file:
        file.write(b"\x00" * FreeBytes)
    
    os.remove(Path)
    print("Done...")

else:
    print("This path could not be found")
    exit