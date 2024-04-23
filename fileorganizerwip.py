# import os to allow work with computer files 
# i will be using Pythons shutil module

import os 
import shutil

# define function 

def fileOrganizer():

        files = [f for f in os.listdir('.') if os.path.isfile(f)]

# organize the file types that will belong to each folder 

    FileTypes = {
        "Photos" = [".png", ".jpeg", ".jpg", ".gif", ],
        "Videos" = [".mp4", ".mov", ".wmv"],
        "Music" = [".mp3", ".wav"],
        "Documents" = [".doc", ".docx", ".pdf", ".ppt",".xlsx"]

    }

