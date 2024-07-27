# We have attendance files inside a folder with the month name and we want to rename the attendance files by adding the month name as a prefix

from pathlib import Path 

root_dir = Path ('Automate-the-boring-stuff/Working-With-Files/attendance')
file_paths = root_dir.glob('**/*')

for path in file_paths:
    if path.is_file():
        print (path.parts)
        parent_folder = path.parts[-2]
        print(parent_folder)
        new_filename = parent_folder + '-' + path.name 
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)

