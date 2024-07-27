#Renaming all files inside a folder by giving them a prefix new-
from pathlib import Path

root_dir = Path ('Automate-the-boring-stuff/Working-With-Files/files') # out root folder
file_paths = list (root_dir.iterdir()) # list of file and directories inside files folder
print(file_paths)

for path in file_paths:
    if path.is_file(): # check if it's a file, so as to not rename folder names
        new_file_name = "new-" + path.name # append the prefix to the file name
        print(new_file_name)
        new_filepath = path.with_name(new_file_name) # create a new path with the folder and new file name
        print(new_filepath)
        path.rename(new_filepath) # rename the files