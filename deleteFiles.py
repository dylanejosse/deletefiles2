from pathlib import Path
import os

def deleteAll(directory):
    p = Path(directory)
    for i in p.iterdir():
        if os.path.isfile(i):
            os.remove(i)
        elif os.path.isdir(i):
            os.rmdir(i)

deleteAll(input("What is the folder that you want to delete all the content ? Please give me the path of it : "))