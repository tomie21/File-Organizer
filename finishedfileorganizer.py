import os
import shutil
from pathlib import Path

FileTypes = {
    "Photos": [".png", ".jpeg", ".jpg", ".gif",],
    "Videos": [".mp4", ".mov", ".wmv"],
    "Music": [".mp3", ".wav"],
    "Documents": [".doc", ".docx", ".pdf", ".ppt",".xlsx"],
}

#insert your file destination path here
os.chdir("C:\\Users\\Admin\\Downloads")

currentDirectory = Path.cwd()


for filename in os.listdir(currentDirectory):
    if os.path.isfile(filename):
        # Get the file extension
        _, ext = os.path.splitext(filename)

        for folder, extensions in FileTypes.items():
            if ext.lower() in extensions:
                folder_path = currentDirectory / folder
                folder_path.mkdir(exist_ok=True)
                shutil.move(filename, folder_path / filename)

print("Your files are now organized!")