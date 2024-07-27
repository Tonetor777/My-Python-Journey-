from pathlib import Path

# Define path objects
filepath = Path("Automate-the-boring-stuff/Working-With-Files/files/abcd.txt")
folderpath = Path("files")

# Check if the folder exists, if not, create it
if not folderpath.exists():
    folderpath.mkdir(parents=True, exist_ok=True)

print(type(filepath)) # Path object

# Check if the file exists, if not, create and write to it
if not filepath.exists():
    with open(filepath, 'w') as file: # Create and open file for writing
        print(file.write("Created file")) # Write to the file

print(filepath.name) # File name
print(filepath.stem) # File name without the extension
print(filepath.suffix) # Only the extension

# List files and directories in the folder
for items in folderpath.iterdir():
    print(items)
